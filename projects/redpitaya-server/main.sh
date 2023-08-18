#!/bin/bash
gpid=0

# command="python3 demo.py"
command="bash ./demo.sh"

start() {
  pkill -9 -f ICING
  bash -c "exec -a ICING $command $1" &
  echo "$gpid"
}

stop(){
  rm -f ./data/convergence.csv ./data/spingrid.csv
  pkill -9 -f ICING
}

"$@"