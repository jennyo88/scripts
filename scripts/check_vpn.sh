#!/usr/bin/env bash

# Set MQTT broker address and topic
MQTTHOST="192.168.0.213"
TOPIC="network/jail/burra"

# Predefined URLs for ping and curl
ping_url="war6000.mooo.com"
curl_url="icanhazip.com"

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
    VPNStat="OFF"
else
    VPNStat="ON"
fi

# Assign result to the variable VPNStat
echo "VPNStat: $VPNStat"

# Publish VPN status on MQTT
/usr/local/bin/mosquitto_pub -h "$MQTTHOST" -t "$TOPIC" -m "$VPNStat"

# If VPNStat is "OFF", stop transmission service
if [ "$VPNStat" = "OFF" ]; then
    echo "Stopping transmission service..."
    service transmission stop
    exit 1
fi

# If VPNStat is "ON" and transmission service is not running, start the service
if [ "$VPNStat" = "ON" ] && service transmission status | grep -q 'not running'; then
    echo "VPN is ON and transmission service is not running, starting transmission service..."
    service transmission start
fi
