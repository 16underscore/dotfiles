#!/bin/sh
xrandr --output HDMI-1 --mode 1920x1080 --rate 120 --primary --output VGA-1 --left-of HDMI-1 --mode 1920x1080 --rate 60
setxkbmap -layout de
[[ -f ~/.Xresources ]] && xrdb -merge -I$HOME ~/.Xresources
herbstluftwm --locked
