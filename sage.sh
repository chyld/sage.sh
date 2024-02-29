#!/usr/bin/env bash

shellsage() {
    local prompt="$*"
    local filename="$HOME/Documents/sage.sh/$(date '+%Y-%m-%d-%H-%M-%S').md"
    echo -n "$prompt" | sage.py 1> "$filename"
    bat --style full "$filename"
}

alias ss=shellsage

