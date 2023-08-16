#!/bin/bash
gpid=0

command="python3 demo.py"

start() {
  bash -c "exec -a ICING $command" &
  echo "$gpid"
}

stop(){
  pkill -9 -f ICING
}

"$@"