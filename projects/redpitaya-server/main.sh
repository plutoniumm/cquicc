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
  pkill -9 -f ICING

  date=$(date +%s)
  mv ./data/convergence.csv ./data/convergence_$date.csv
  mv ./data/spingrid.csv ./data/spingrid_$date.csv
}

"$@"