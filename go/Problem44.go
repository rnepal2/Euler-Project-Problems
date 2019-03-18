package main

import (
	"fmt"
	"math"
	"time"
)

// check if a number is pentagonal
func isPentagonal(n int) bool {
	pentagonal := false
	// out of the two solutions: only one is positive
	solution := (1 + math.Sqrt(float64(1+24*n))) / 6 
	if math.Mod(solution, 1.0) == 0 {
		pentagonal = true
	}
	return pentagonal
}

// absoulte value of an integer 
func Abs(n int) int {
	if n < 0 { 
		return -n
	} else {
		return n
	}
}

// main function
func main() {
	start := time.Now()

	var reqPairs []int
	var pentagonalSlice []int
	
	for i := 1; i <=5000; i++ {
		pentagonalSlice = append(pentagonalSlice, int(i*(3*i - 1)/2))
	}
	
	for j, pj := range pentagonalSlice {
		for k := j; k < len(pentagonalSlice); k++ {
			pk := pentagonalSlice[k]
			sum := pj + pk
			diff := Abs(pj - pk)
			save := []int{pj, pk, diff}
			if isPentagonal(sum) == true && isPentagonal(diff) == true {
				reqPairs = append(reqPairs, save...)
			}
			// avoiding two very far apart pentagonal numbers (need min diff)
			if Abs(j - k) > 50 { 
				continue 
			}
		}
	}
	// print result
	fmt.Println("The two required numbers and their difference are: ", reqPairs)
	fmt.Println("Answer: D = ", reqPairs[2])
	elapsed := time.Since(start)
	fmt.Println("Total run time: ", elapsed)
}
