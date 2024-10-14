#!/bin/bash
# Change the theme of the system
if [ -n "$1" ]; then
	THEME="$1"
else
	THEME=$(./download_theme.py | rofi -dmenu -p "Select theme")
	if [ -z "$THEME" ]; then
		exit 0
	fi
	if [ ! -e "colors/$THEME.hex" ]; then
		./download_theme.py "$THEME"
		./format_hex_file.py "$(realpath "colors/$THEME")" > "colors/$THEME.hex"
		rm "colors/$THEME"
	fi
	./generate_theme.py "$(realpath "colors/$THEME.hex")"
fi
pgrep polybar && killall polybar >/dev/null
sleep 0.2
bspc wm -r
