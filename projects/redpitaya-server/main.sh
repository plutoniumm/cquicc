#!/bin/bash
gpid=0

# command="python3 demo.py"
command="./demo"

start() {
  pkill -9 -f ICING
  bash -c "exec -a ICING $command $1" &
  echo "$gpid"
}

stop(){
  pkill -9 -f ICING
}

"$@"