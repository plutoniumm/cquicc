#!/bin/bash
pid=0

run(){
  ./a.out &
  pid=$!
  echo "pid: $pid"
}

stop(){
  kill -9 $pid
}

"$@"