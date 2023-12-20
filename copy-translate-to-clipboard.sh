#!/bin/bash
# Path to your beep sound file (change this to the path of your sound file)
BEEP_SOUND="/home/ri/Desktop/Projects/google-translate/beep-07a.wav"

# Get the content from the clipboard
SELECTED_TEXT=$(xclip -o)

# Play beep sound before running the Python script
aplay "$BEEP_SOUND" &>/dev/null || paplay "$BEEP_SOUND" &>/dev/null

# Run the Python script with the clipboard content
python3.9 /home/ri/Desktop/Projects/google-translate/googletranslate.py -r "plain" 'fa' "$SELECTED_TEXT"

# Play beep sound after running the Python script
aplay "$BEEP_SOUND" &>/dev/null || paplay "$BEEP_SOUND" &>/dev/null
