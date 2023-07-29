#!/bin/bash

# Define the log file path
LOG_FILE="./usb-monitor.log"

# Get the initial list of connected USB devices
initial_devices=$(lsusb)

# Function to log the events
log_event() {
    local event_time="$(date +'%Y-%m-%d %H:%M:%S')"
    local event_type="$1"
    local device_id="$2"

    echo "$event_time | $event_type | $device_id" >> "$LOG_FILE"
}

# Function to check for new devices
check_devices() {
    while true 
    do
        current_devices=$(lsusb)
        echo "$initial_devices" | sort > "./idev.txt"
        echo "$current_devices" | sort > "./cdev.txt"
        new_devices=$(comm -13 "./idev.txt" "./cdev.txt")
        removed_devices=$(comm -13 "./cdev.txt" "./idev.txt")
        if test "$new_devices" != ""
        then
            for device in "$new_devices"; do
                log_event "connected" "$device"
            done
        fi
        if test "$removed_devices" != ""
        then
            for device in "$removed_devices"; do
                log_event "disconnected" "$device"
            done
        fi
        initial_devices=$current_devices
        sleep 1  # Adjust the update interval as needed
    done
}

# Start monitoring, just call check_devices()
check_devices
