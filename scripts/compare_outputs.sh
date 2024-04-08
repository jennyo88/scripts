#!/usr/bin/env bash

# Bash script to compare two outputs provided as command-line arguments.
##
## Sample command:
## ./compare_outputs.sh "$(ping -c 4 example.com)" "$(curl -s https://example.com)"
##

# Check if the number of arguments is not equal to 2
if [ "$#" -ne 2 ]; then
    echo "Usage: $0 <ping_output> <curl_output>"
    exit 1
fi

# Assign arguments to variables
ping_output="$1"
curl_output="$2"

# Compare outputs
if [ "$ping_output" = "$curl_output" ]; then
    echo "The outputs are the same."
else
    echo "The outputs differ:"
    echo ""
    echo "Ping Output:"
    echo "$ping_output"
    echo ""
    echo "Curl Output:"
    echo "$curl_output"
fi
