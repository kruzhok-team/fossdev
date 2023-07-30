#!/bin/bash
website="https://example.com"
response=$(curl -Is "$website" | head -n 1)
if [[ "$response" == *"200 OK"* ]]; then
    echo "Website is reachable."
else
    echo "Website is down or unreachable."
fi
