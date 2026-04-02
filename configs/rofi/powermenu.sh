#!/bin/bash
options="⏻ Shutdown\n Reboot\n Suspend\n Logout"
chosen=$(echo -e "$options" | rofi -dmenu -i -p "Power" -theme /home/KJ/.config/rofi/cyberpunk.rasi)
case $chosen in
    "⏻ Shutdown") systemctl poweroff ;;
    " Reboot") systemctl reboot ;;
    " Suspend") systemctl suspend ;;
    " Logout") hyprctl dispatch exit ;;
esac
