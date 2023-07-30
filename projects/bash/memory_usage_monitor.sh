#!/bin/bash

# File to store the memory usage data
output_file="memory_usage_log.txt"

# Header for the output file (if it doesn't exist)
if [ ! -f "$output_file" ]; then
    echo "Datetime Memory_Usage(KB)" > "$output_file"
fi

# Function to get memory usage of the process by PID
get_memory_usage() {
    local pid=$1
    local memory_usage=$(ps -o rss= -p "$pid" | awk '{ sum+=$1 } END { print sum }')
    echo "$memory_usage"
}

# Check if a process ID was provided as an argument
if test -z "$1" ; then
    echo "Usage: $0 <process_id>"
    exit 1
fi

# Main loop to monitor and log memory usage
while true; do
    datetime=$(date +"%Y-%m-%d %H:%M:%S")
    pid="$1"
    memory_usage=$(get_memory_usage "$pid")

    # Append data to the output file
    echo "$datetime $memory_usage" >> "$output_file"

    # Wait for 1 second before the next iteration
    sleep 1
done
