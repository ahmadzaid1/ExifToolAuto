
Automating the process of removing metadata from files using ExifTool.


## Prerequisites
Before running the script, ensure you have the following installed:
- [ExifTool](https://exiftool.org/)
- [watchdog](https://github.com/gorakhargosh/watchdog)  (for monitoring the Downloads directory).

## Installation
1. Clone the Repository.
```bash
git clone https://github.com/ahmadzaid1/ExifToolAuto.git
cd ExifToolAuto
```
2. Make the script executable.
```bash
chmod +x metaDataRemover.py
```
3. Run the script:
```bash 
python3 metaDataRemover.py
```
This script will start monitoring the Downloads directory for new files and automatically remove their metadata.

## Setting Up the Script to Run on Startup
By default, the script will stop working if the session is closed or the computer is shut down. To ensure the script runs automatically every time you turn on your computer, you can add it as a service to your `systemd`.
Open a terminal and create a new service unit file for your script. For example:
1. Create a systemd Service Unit File:
```bash 
sudo nano /etc/systemd/system/metaDataRemover.service
```
2. Add Service Configuration:
```bash
[Unit]
Description=Metadata Remover Service
After=network.target

[Service]
Type=simple
User=yourusername
ExecStart=/usr/bin/python3 /path/to/metaDataRemover.py
WorkingDirectory=/path/to/Downloads/directory
Restart=on-failure

[Install]
WantedBy=multi-user.target
```
3. Save and Close the File

  In Nano, press `Ctrl+O`, then `Enter` to save the file. Press `Ctrl+X` to exit Nano.
  
4. Reload systemd:
```bash
sudo systemctl daemon-reload
```
5. Enable the Service to Start on Boot:
```bash
sudo systemctl enable metaDataRemover.service
```
6. Start the Service:
```bash
sudo systemctl status metaDataRemover.service
```
## Original ExifTool Repository

This repository provides scripts to automate the process of removing metadata from files using ExifTool. For more information about ExifTool and its usage, you can refer to the original ExifTool repository.

-   **ExifTool Repository**: [exiftool/exiftool](https://github.com/exiftool/exiftool)
## Log file
The remove_metadata.sh script logs its actions to a file named metadata_removal.log in the Downloads directory. This log file contains information about each file processed by the script.
## License

This project is licensed under the [The Unlicense](https://unlicense.org/) - see the [LICENSE](https://github.com/ahmadzaid1/ExifToolAuto/blob/main/LICENSE) file for details.

