#!/usr/bin/env bash
xrandr --output LVDS1 --auto -s 1366x768
xrandr --output HDMI1 --auto -s 1920x1080 --right-of LVDS1
