#!/bin/bash
# Change the theme of the system

CONFIG_DIR="$HOME/.config"
if [ -n "$1" ]; then
	BASEDIR="$1"
else
	BASEDIR=$(./main.py | rofi -dmenu -p "Select theme")
	if [ -z "$BASEDIR" ]; then
		exit 0
	fi
fi

echo "Changing theme to $BASEDIR"
./main.py "$BASEDIR"

cp "$BASEDIR/i3_colors" "$CONFIG_DIR/i3"
i3-msg reload > /dev/null
cat "$BASEDIR/alacritty_colors" > "$CONFIG_DIR/alacritty/alacritty_tmp"
tail -30 "$CONFIG_DIR/alacritty/alacritty.toml" >> "$CONFIG_DIR/alacritty/alacritty_tmp" 
mv "$CONFIG_DIR/alacritty/alacritty_tmp" "$CONFIG_DIR/alacritty/alacritty.toml"
#mv "$BASEDIR/polybar_colors" "$CONFIG_DIR/polybar"
#mv "$BASEDIR/tmux_colors" "$CONFIG_DIR/tmux/tmux_colors.conf"
