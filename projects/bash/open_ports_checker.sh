#!/bin/bash

# Remote website to check (replace example.com and 80 with the appropriate values)
remote_host="example.com"
port="80"

# Function to check if the port is open on the remote site
check_port_open() {
    local host=$1
    local port=$2
    nc -z -w5 "$host" "$port" >/dev/null 2>&1
    if [ $? -eq 0 ]; then
        echo "Port $port is open on $host"
    else
        echo "Port $port is closed or unreachable on $host"
    fi
}

# Call the function to check the port
check_port_open "$remote_host" "$port"
