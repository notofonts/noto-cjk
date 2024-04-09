#!/bin/sh
SERIF_SOURCES=Serif/Variable/TTF/Subset/*ttf
SANS_SOURCES=Sans/Variable/TTF/Subset/*ttf

python3 google-fonts/hotfix.py --output-dir=google-fonts $SERIF_SOURCES $SANS_SOURCES
add-chws -o google-fonts google-fonts/*ttf
