#!/usr/bin/env bash

# kill anothers programs
ps aux | grep 'python .*wallpapers.py' | awk {'print $2'} | xargs kill -9

# Run
python ~/scripts/wallpapers.py &
