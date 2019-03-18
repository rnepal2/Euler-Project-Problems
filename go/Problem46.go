package main 

import (
	"fmt"
	"time"
	)
	
// each number to loop through is of type myNumber
type myNumber struct {
	n int
	odd bool
	composite bool
	Goldbach bool
}

// checks if a number is odd or not
func odd(n int) bool {
	if n % 2 == 0 {
		return false
	} else {
		return true
	}
}

// checks if a number is composite or not
func composite(n int) bool {
	composite := false 
	for i := 2; i < int(n/2)+1; i++ {
		if n % i == 0 {
			composite = true
			break
		}
	}
	return composite
}

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

// checks if a number is Goldbach composite or not
func goldbachComposite(n int) bool {
	Goldbach := false
	for j := 1; j < n; j++ {
		if isPrime(j) == true {
			for k := 1; k < int(n/2); k++ {
				if n == j + 2*k*k {
					Goldbach = true
					break
				}
			}
		}
	}
	return Goldbach
}

func main() {
	start := time.Now()
	i := 1
	for {
		odd := odd(i)
		composite := composite(i)
		Goldbach := goldbachComposite(i)
		num := myNumber{i, odd, composite, Goldbach}
		if num.odd == true && num.composite == true && num.Goldbach == false {
			fmt.Println("First Goldbach composite contradiction: ", num)
			break
		}
		i++
	}
	elapsed := time.Since(start)
	fmt.Println("The total run time is: ", elapsed)
}