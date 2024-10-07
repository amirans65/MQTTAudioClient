#!/bin/bash
#chmod +x check_bluetooth_connection.sh


# Read the MAC address from the JSON config file
CONFIG_FILE="appsettings.json"
MAC_ADDRESS=$(jq -r '.bluetooth.mac_address' "$CONFIG_FILE")

# Check if the device is connected
if bluetoothctl info "$MAC_ADDRESS" | grep -q "Connected: yes"; then
    echo "True"
else
    echo "False"
fi
