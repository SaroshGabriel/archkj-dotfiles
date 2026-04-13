#!/bin/bash
capacity=$(cat /sys/class/power_supply/BAT0/capacity 2>/dev/null || echo 0)
status=$(cat /sys/class/power_supply/BAT0/status 2>/dev/null || echo "Unknown")

if [[ "$status" == "Charging" ]]; then
    echo "󰂄 ${capacity}%"
elif [[ "$capacity" -eq 0 ]]; then
    echo ""
else
    echo "󰁹 ${capacity}%"
fi
