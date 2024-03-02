#!/usr/bin/env bash

shellsage() {
    local context="$1"
    local infile="$HOME/Documents/sage.sh/$(date '+%Y-%m-%d-%H-%M-%S').in.md"
    local outfile="$HOME/Documents/sage.sh/$(date '+%Y-%m-%d-%H-%M-%S').out.md"
    nvim "$infile"
    if [ ! -s "$infile" ]; then echo "The file is empty. Nothing to do."; return 1; fi
    bat "$infile" | sage.py "$context" 1> "$outfile"
    bat --style full "$outfile"
}

alias ss="glow $HOME/.bin/sage.sh/sage.help.md"
alias sst="shellsage terminal"
alias ssp="shellsage python"
alias ssj="shellsage javascript"
alias ssd="cd $HOME/Documents/sage.sh"
alias ssb="cd $HOME/.bin/sage.sh"

