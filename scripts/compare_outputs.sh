#!/usr/bin/env bash

# Bash script to compare the IP address obtained from ping output with the IP address obtained from curl output.

##
## ./compare_outputs.sh "$(ping -c 1 sample.com)" "$(curl -s sample.com)"

# Check if the number of arguments is not equal to 2
if [ "$#" -ne 2 ]; then
    echo "Usage: $0 <ping_output> <curl_output>"
    exit 1
fi

# Function to extract IP address from ping output
get_ip_from_ping() {
    echo "$1" | head -n 1 | awk '{print $3}' | sed 's/[():]//g'
}

# Extract IP address from curl output
get_ip_from_curl() {
    echo "$1"
}

# Assign arguments to variables
ping_output="$1"
curl_output="$2"

# Get IP address from ping output
ping_ip=$(get_ip_from_ping "$ping_output")

# Get IP address from curl output
curl_ip=$(get_ip_from_curl "$curl_output")

# Compare IP addresses (ignoring trailing characters such as colons)
if [ "${ping_ip%"${ping_ip##*[![:space:]]}"}" = "${curl_ip%"${curl_ip##*[![:space:]]}"}" ]; then
    echo "The IP addresses extracted from ping and curl outputs are the same: $ping_ip"
else
    echo "The IP addresses extracted from ping and curl outputs are different:"
    echo "Ping IP: $ping_ip"
    echo "Curl IP: $curl_ip"
fi
