#!/bin/bash

# To use with .po files use this command:
# msgfilter ./apostrophe_normalizer.sh < input.po > output.po

# To use with text files use this command:
# ./apostrophe_normalizer.sh < input.txt > output.txt

sed -E \
    -e "s/([oOgG])['‘]/\1ʻ/g" \
    -e "s/['’]/ʼ/g"

