#!/usr/bin/env bash

## SAMPLE
## ./compare_outputs.sh -p sample.com -c sample.com
## ./compare_outputs.sh --ping sample.com --curl sample.com

# Default values for flags
ping_url=""
curl_url=""

# Parse command-line arguments
while [[ $# -gt 0 ]]; do
    key="$1"
    case $key in
        -p|--ping)
            ping_url="$2"
            shift
            shift
            ;;
        -c|--curl)
            curl_url="$2"
            shift
            shift
            ;;
        *)
            echo "Unknown option: $1"
            exit 1
            ;;
    esac
done

# Check if both ping and curl URLs are provided
if [ -z "$ping_url" ] || [ -z "$curl_url" ]; then
    echo "Usage: $0 -p <ping_url> -c <curl_url>"
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

# Get IP address from ping command
ping_output=$(ping -c 1 "$ping_url")
ping_ip=$(get_ip_from_ping "$ping_output")

# Get IP address from curl command
curl_output=$(curl -s "$curl_url")
curl_ip=$(get_ip_from_curl "$curl_output")

# Compare IP addresses (ignoring trailing characters such as colons)
if [ "${ping_ip%"${ping_ip##*[![:space:]]}"}" = "${curl_ip%"${curl_ip##*[![:space:]]}"}" ]; then
    echo "The IP addresses extracted from ping and curl outputs are the same: $ping_ip"
else
    echo "The IP addresses extracted from ping and curl outputs are different:"
    echo "Ping IP: $ping_ip"
    echo "Curl IP: $curl_ip"
fi
