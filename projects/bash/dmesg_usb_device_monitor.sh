#!/bin/bash
prev_records=$(dmesg | tail -20)
 
monitor_devices_records() {

    while true
    do
        curr_records=$(dmesg | tail -20)
        new_records=$(comm -13 <(echo "$prev_records") <(echo "$curr_records"))
        usb_records=$(echo "$new_records" | grep usb)
        if test "$usb_records" != ""
        then
            echo "$usb_records"
        fi
        prev_records=$curr_records
    done
}
# Start monitoring
monitor_devices_records
