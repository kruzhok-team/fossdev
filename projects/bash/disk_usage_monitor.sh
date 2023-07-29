#!/bin/bash
monitor_device=$1  #device to monitor eg. /dev/sdc1
alert_level=$2     #available percentage to alert eg. 1
 
monitor_space_usage() {

    while true
    do
        df_record=$(df | grep "$monitor_device")
        df_record_array=($df_record)
        avail=${df_record_array[3]}
        total=${df_record_array[1]}
        if test $(( 100 * $avail / $total)) -le $alert_level
        then
            echo "Alert disk is almost full"
        fi
        sleep 1
    done
}

monitor_space_usage
