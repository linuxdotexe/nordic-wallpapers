#!/usr/bin/env bash

# enter list of wallpapers into wallpaper-preview.md
ls wallpapers/ > wallpaper-preview.md
# add image preview command thing for markdown in prefix and suffix
sed -i -e 's/^/![](wallpapers\//' wallpaper-preview.md
sed -i 's/$/\)/' wallpaper-preview.md
# add the page heading back on
sed -i '1 i\# Wallpapers in this repository' wallpaper-preview.md
# add empty line to look good
sed -i '/# Wallpapers/ a \ ' wallpaper-preview.md
