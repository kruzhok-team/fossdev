#!/bin/bash

file="/path/to/watched/file"
substring="critical error"

if grep -q "$substring" "$file"; then
    echo "Found critical error in $file"
    # Add your notification command here, e.g., sendmail or notify-send
else
    echo "No critical error found in $file"
fi
