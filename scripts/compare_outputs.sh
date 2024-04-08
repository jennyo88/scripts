#!/usr/bin/env bash

# Bash script to compare two outputs provided as command-line arguments.

# Check if the number of arguments is not equal to 2
if [ "$#" -ne 2 ]; then
    echo "Usage: $0 <output1> <output2>"
    exit 1
fi

# Assign arguments to variables
output1="$1"
output2="$2"

# Compare outputs line by line
IFS=$'\n' read -r -a lines1 <<< "$output1"
IFS=$'\n' read -r -a lines2 <<< "$output2"

for i in "${!lines1[@]}"; do
    if [ "${lines1[$i]}" != "${lines2[$i]}" ]; then
        echo "The outputs differ at line $((i+1)):"
        echo "Output 1: ${lines1[$i]}"
        echo "Output 2: ${lines2[$i]}"
        exit 0
    fi
done

# If no differences found
echo "The outputs are the same."
