Automating the process of removing metadata from files using ExifTool.


# Prerequisites
- [ExifTool](https://exiftool.org/)
- [inotify-tools](https://github.com/inotify-tools/inotify-tools)  (for monitoring the Downloads directory).

# Installation
1. Clone the Repository.
```bash
git clone https://github.com/ahmadzaid1/ExifToolAuto.git
cd ExifToolAuto
```
2. Make the scripts executable.
```bash
chmod +x remove_metadata.sh 
chmod +x watch_downloads.sh
```
# Usage 
1. Run the Watcher Script:
```bash 
./watch_downloads.sh
```
This script will start monitoring the Downloads directory for new files and automatically remove their metadata.

# Setting Up the Script to Run on Startup
By default, the script will stop working if the session is closed or the computer is shut down. To ensure the script runs automatically every time you turn on your computer, you can add it to your `crontab`.
```sh
crontab -e
@reboot /path/to/your/script/watch_downloads.sh`
```
# Configuration
### Overwriting Files

By default, the script does not overwrite the original file. Instead, it creates a new file with `_metadataremoved` appended to the filename.

To enable overwriting of the original file, change `OVERWRITE=false` to `OVERWRITE=true` in `remove_metadata.sh`.
```bash
OVERWRITE=true
```
# Original ExifTool Repository

This repository provides scripts to automate the process of removing metadata from files using ExifTool. For more information about ExifTool and its usage, you can refer to the original ExifTool repository.

-   **ExifTool Repository**: [exiftool/exiftool](https://github.com/exiftool/exiftool)
# Log file
The remove_metadata.sh script logs its actions to a file named metadata_removal.log in the same directory as the script. This log file contains information about each file processed by the script.
