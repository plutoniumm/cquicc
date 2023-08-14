#!/bin/bash
echo "PID: $$"
NUM=$(date +%s)
FILE="./send.txt"
ITERS=50

while :; do
  echo "Running on Num: $NUM"
  echo "x,y,z" > $FILE
  for (( x=0; x<=$ITERS; x++ )); do
      for (( y=0; y<=$ITERS; y++ )); do
        NUM=$(((NUM * 1103515245 + 12345) % 65536));
        NUM=$((NUM / 100));
        RND=$((NUM % 2));

        echo "$x,$y,$RND" >> $FILE
      done
  done
  sleep 1
done