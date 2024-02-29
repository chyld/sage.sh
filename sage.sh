#!/usr/bin/env bash

shellsage() {
    local infile="$HOME/Documents/sage.sh/$(date '+%Y-%m-%d-%H-%M-%S').in.md"
    local outfile="$HOME/Documents/sage.sh/$(date '+%Y-%m-%d-%H-%M-%S').out.md"
    nvim "$infile"
    bat "$infile" | sage.py 1> "$outfile"
    bat --style full "$outfile"
}

alias ss=shellsage
alias ssd="cd $HOME/Documents/sage.sh"

