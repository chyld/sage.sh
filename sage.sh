#!/usr/bin/env bash

shellsage() {
    local input="$*"
    local tempfile="/tmp/mytempfile.$$.$RANDOM.md"
    echo -n "$input" | "/home/chyld/Xplore/Temp/kosmogleam-erbium-alpha-2024-0228.541/index.js" 1>"$tempfile"
    glow "${tempfile}"
    rm "${tempfile}"
}

alias ss=shellsage
