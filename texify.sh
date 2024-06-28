#!/bin/bash
if [ $# -eq 0 ]; then
  echo "No arguments supplied"
  exit 1
fi

if [ ! -f $1 ]; then
  if [ ! -f $1.md ]; then
    echo "File not found!";
    exit 1;
  fi
fi

filename=$(basename -- "$1")
extension="${filename##*.}"
filename="${filename%.*}"

pandoc -s --to=latex --from=markdown $1