#!/bin/bash
WALLPAPER_DIR="$HOME/Pictures/Wallpapers"

mapfile -t walls < <(find "$WALLPAPER_DIR" -type f \( -name "*.jpg" -o -name "*.png" -o -name "*.jpeg" \))

sleep 2

while true; do
    wall1="${walls[$RANDOM % ${#walls[@]}]}"
    wall2="${walls[$RANDOM % ${#walls[@]}]}"
    awww img --outputs HDMI-A-2 --transition-type random "$wall1" &>/dev/null
    awww img --outputs eDP-1 --transition-type random "$wall2" &>/dev/null
    sleep 300
done
