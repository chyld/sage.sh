#!/usr/bin/env bash

shellsage() {
    local input="$*"
    local tempfile="/tmp/mytempfile.$$.$RANDOM.md"
    echo -n "$input" | "./index.js" 1>"$tempfile"
    glow "${tempfile}"
    rm "${tempfile}"
}

alias ss=shellsage

