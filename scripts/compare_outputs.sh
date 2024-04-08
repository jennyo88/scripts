#!/usr/bin/env bash

# Predefined URLs for ping and curl
ping_url="sample.com"
curl_url="sample.com"

# Function to extract IP address from ping output
get_ip_from_ping() {
    echo "$1" | head -n 1 | awk '{print $3}' | sed 's/[():]//g'
}

# Extract IP address from curl output
get_ip_from_curl() {
    echo "$1"
}

# Get IP address from ping command
ping_output=$(ping -c 1 "$ping_url")
ping_ip=$(get_ip_from_ping "$ping_output")

# Get IP address from curl command
curl_output=$(curl -s "$curl_url")
curl_ip=$(get_ip_from_curl "$curl_output")

# Compare IP addresses (ignoring trailing characters such as colons)
if [ "${ping_ip%"${ping_ip##*[![:space:]]}"}" = "${curl_ip%"${curl_ip##*[![:space:]]}"}" ]; then
    echo "VPN down"
else
    echo "Canada"
fi
