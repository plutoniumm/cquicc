package main

import (
	"fmt"
	"math"
	"math/rand"
	"os"
	"strconv"
	"strings"
	"time"
)

const (
	DATA_FILE     = "./data/spingrid.csv"
	LOSS_FILE     = "./data/convergence.csv"
	SAFETY_CUTOFF = 100
)

func rando() string {
	return strconv.Itoa(rand.Intn(2))
}

func generateValues(n int) string {
	var result strings.Builder

	for x := 0; x < n; x++ {
		for y := 0; y < n; y++ {
			result.WriteString(rando())
			if y < n-1 {
				result.WriteString(",")
			}
		}
		if x < n-1 {
			result.WriteString("\n")
		}
	}

	return result.String()
}

func calculateLoss(n int) string {
	var result strings.Builder
	for x := 0; x < 100-n; x++ {
		rt := math.Sqrt(float64(x))
		jitter := 0.25 * rt
		y := 10 - rt + jitter

		res := strconv.Itoa(x) + "," + strconv.FormatFloat(y, 'f', 2, 64)
		if x < 99-n {
			res += "\n"
		}
		result.WriteString(res)
	}

	return result.String()
}

func main() {
	// Delete old files
	err := os.Remove(DATA_FILE)
	err = os.Remove(LOSS_FILE)
	if err != nil {
	} // we dont care

	loops := SAFETY_CUTOFF
	for loops > 0 {
		fmt.Printf("Running loop %d\n", loops)

		n, _ := strconv.Atoi(os.Args[1])

		fp, _ := os.Create(DATA_FILE)
		fp.WriteString(generateValues(n))
		fp.Close()

		fp2, _ := os.Create(LOSS_FILE)
		fp2.WriteString(calculateLoss(loops))
		fp2.Close()

		loops--
		time.Sleep(time.Second)
	}
}
