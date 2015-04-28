#!/usr/bin/env bash

# kill anothers programs
ps aux | grep -i wallpaper..py | awk {'print $2'} | xargs kill -9

# Run
python ~/scripts/wallpapers.py &
