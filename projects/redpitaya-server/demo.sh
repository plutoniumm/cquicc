#!/bin/bash
function rando {
    echo $((RANDOM % 2))
}

function generateValues {
    local n=$1
    local result=""

    for ((x=0; x<n; x++)); do
        for ((y=0; y<n; y++)); do
            result+="$(rando)"
            if ((y < n - 1)); then
                result+=","
            fi
        done
        if ((x < n - 1)); then
            result+="\n"
        fi
    done

    echo -e "$result"
}

function calculateLoss {
    local n=$1
    local result=""

    for ((x=0; x<100-n; x++)); do
        rt=$(bc -l <<< "sqrt($x)")
        jitter=$(bc -l <<< "0.25 * $rt")
        y=$(bc -l <<< "10 - $rt + $jitter")

        res="$x,$(printf "%.2f" $y)"
        if ((x < 99 - n)); then
            res+="\n"
        fi
        result+="$res"
    done

    echo -e "$result"
}

DATA_FILE="./data/spingrid.csv"
LOSS_FILE="./data/convergence.csv"
SAFETY_CUTOFF=100

rm -f "$DATA_FILE" "$LOSS_FILE"

loops=$SAFETY_CUTOFF
while [ "$loops" -gt 0 ]; do
    echo "Running loop $loops"

    n="$1"
    generateValues "$n" > "$DATA_FILE"
    calculateLoss "$loops" > "$LOSS_FILE"
    loops=$((loops - 1))
    sleep 1
done
