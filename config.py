theme_sources = {
        'i3': 'tinted-theming/base16-i3/main/colors/base16-',
        'alacritty': "aarowill/base16-alacritty/master/colors/base16-",
        'dunst': "tinted-theming/base16-dunst/master/themes/base16-",
        'polybar': "tinted-theming/base16-polybar/main/colors/base16-",
        'rofi': "tinted-theming/base16-rofi/master/colors/base16-",
        'tmux': "tinted-theming/tinted-tmux/master/colors/base16-"
        }

theme_configurations = [
        ('i3', '.config', 'i3_colors'),
        ('alacritty', '.toml', 'alacritty_colors'),
        ('dunst', '.dunstrc', 'dunst_colors'),
        ('polybar', '.ini', 'polybar_colors'),
        ('rofi', '.rasi', 'rofi_colors'),
        ('tmux', '.conf', 'tmux_colors')
        ]
