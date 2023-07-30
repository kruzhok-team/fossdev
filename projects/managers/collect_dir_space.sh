#!/bin/bash

target_directory="/tmp/monitored_directory"

log_file="/tmp/dir_space.log"

# Collect disk space occupied by the target directory
disk_space=$(du -sh "$target_directory")

current_date=$(date +"%Y-%m-%d %H:%M:%S")

# Log the disk space information with the current date
echo "$current_date - Disk Space Usage: $disk_space" >> "$log_file"
