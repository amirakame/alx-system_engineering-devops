#!/usr/bin/env bash
# This script checks if all files in the current directory end with a new line

for file in *; do
if [[ -f $file ]]; then
last_char=$(tail -c 1 "$file")
if [[ $last_char != $'\n' ]]; then
echo "File $file does not end with a new line"
fi
fi
done
