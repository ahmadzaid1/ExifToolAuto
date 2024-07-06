import os
import subprocess
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

DOWNLOADS_DIR = os.path.expanduser("~/Downloads")  # Change this to your desired directory
LOG_FILE = os.path.join(DOWNLOADS_DIR, "metadata_removal.log")


class DownloadEventHandler(FileSystemEventHandler):
    def __init__(self):
        super().__init__()
        self.unsupported_files = set()

    def on_created(self, event):
        if not event.is_directory:
            file_path = event.src_path
            self.process_file(file_path)

    def process_file(self, file_path):
        # Check if the file has already been processed (renamed)
        if "_metadataremoved" in file_path:
            return

        new_file_path = self.get_new_file_path(file_path)

        try:
            # Process the file with ExifTool
            result = subprocess.run(["exiftool", "-all=", file_path, "-o", new_file_path], check=True, capture_output=True, text=True)
            self.log(f"Metadata removed from {file_path}")
        except subprocess.CalledProcessError as e:
            # Log error
            self.log(f"Error removing metadata from {file_path}: {e.stderr}")
            # Log unsupported file type only if not already logged
            if not os.path.splitext(file_path)[1] in self.unsupported_files:
                self.log(f"** File type {os.path.splitext(file_path)[1]} might not be supported by ExifTool. Skipping processing. **")
                self.unsupported_files.add(os.path.splitext(file_path)[1])

    def get_new_file_path(self, file_path):
        dir_name = os.path.dirname(file_path)
        base_name = os.path.basename(file_path)
        name, ext = os.path.splitext(base_name)
        new_file_path = os.path.join(dir_name, f"{name}_metadataremoved{ext}")
        return new_file_path

    def log(self, message):
        with open(LOG_FILE, "a") as log_file:
            log_file.write(f"{time.strftime('%Y-%m-%d %H:%M:%S')} - {message}\n")


if __name__ == "__main__":
    event_handler = DownloadEventHandler()
    observer = Observer()
    observer.schedule(event_handler, DOWNLOADS_DIR, recursive=False)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
