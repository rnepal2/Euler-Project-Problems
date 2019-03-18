package main

import (
	"fmt"
	"time"
)

// decides if a number n is prime or not
func isPrime(n int) bool {
	prime := true
	if n==2 || n==3 || n==5 || n==7 {return true}
	if n%2==0 || n%3==0 || n%5==0 || n%7==0 {return false}
	for i := 2; i < n; i++ {
		if n%i == 0 {
			prime = false
			break
		}
	}
	return prime
}

// returns a slice of required prime numbers below n
func primesList(n int) []int {
	var primesSlice []int // slice of prime numbers
	for i := 2; i < int(n/2); i++ {
		prime := isPrime(i)
		if prime == true {
			primesSlice = append(primesSlice, i)
		}
	}
	return primesSlice
}

// a number and its number of prime factors
type numFactors struct {
	number  int
	pFactors int
}

// numFactors method: updates a number with its number of distinct prime factors
func (a numFactors) Factors(primesSlice *[]int) numFactors {
	var factors []int
	for i, val := range *primesSlice {
		if a.number % val == 0 {
			factors = append(factors, val)
		}
		if a.number < int((*primesSlice)[i]/2) {
			break
		}
	}
	a.pFactors = len(factors)
	return a
}

func main() {
	// start time
	start := time.Now()
	// look for prime numbers (as factor) below n
	// Warning: smaller n might avoid some of the smaller numbers cases
	n := 1500
	primesSlice := primesList(n)

	ncons, i := 0, 645 // ncons = n consecutive numbers; i = start looking after i
	a := numFactors{2, 1}
	for {
		a.number = i
		if a.Factors(&primesSlice).pFactors == 4 { ncons += 1} else { ncons = 0 }
		if ncons == 4 { break }
		i += 1
	}
	// Printing result
	fmt.Println("Such four numbers: ", a.number-3, a.number-2, a.number-1, a.number)
	elapsed := time.Since(start)
	fmt.Println("Total time taken: ", elapsed)
}
