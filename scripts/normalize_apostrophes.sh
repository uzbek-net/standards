#!/bin/bash

# To use with .po files use this command:
# ./apostrophe_normalizer.sh input.txt

# To use with text files use this command:
# ./apostrophe_normalizer.sh input.txt

tmp="$(mktemp)"

sed -E \
    -e "s/([oOgG])['‘]/\1ʻ/g" \
    -e "s/['’]/ʼ/g" \
    "$1" > "$tmp" && mv "$tmp" "$1"