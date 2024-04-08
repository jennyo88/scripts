#!/usr/bin/env bash

# Bash script to compare two outputs provided as command-line arguments.

# Check if the number of arguments is not equal to 2
if [ "$#" -ne 2 ]; then
    echo "Usage: $0 <ping_output> <curl_output>"
    exit 1
fi

# Assign arguments to variables
ping_output="$1"
curl_output="$2"

# Compare outputs line by line
IFS=$'\n' read -r -a lines1 <<< "$ping_output"
IFS=$'\n' read -r -a lines2 <<< "$curl_output"

for i in "${!lines1[@]}"; do
    if [ "${lines1[$i]}" != "${lines2[$i]}" ]; then
        echo "The outputs differ at line $((i+1)):"
        echo "Ping Output: ${lines1[$i]}"
        echo "Curl Output: ${lines2[$i]}"
        exit 0
    fi
done

# If no differences found
echo "The outputs are the same."
