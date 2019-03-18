package main

import (
	"fmt"
	"time"
)

type DateStruct struct {
	day      int
	monthday int
	month    int
	year     int
}

/*
// add methods to the struct
func (date DateStruct) month() int {


}
*/

func main() {
	start := time.Now()
	// var day, monthday, month, year int
	now := DateStruct{day: 2, monthday: 1, month: 1, year: 1901}
	// Calender: keeps the information of every day in the DateStruct format
	calender := []DateStruct{}

	i := 0
	for {
		// increase day: simple and no exceptions
		if now.day == 7 {
			now.day = 1
		} else {
			now.day += 1
		}
		// different months
		month := now.month
		switch month {
		// if months are those with 31 days in that month
		case 1, 3, 5, 7, 8, 10:
			if now.monthday == 31 {
				now.month += 1
				now.monthday = 1
			} else {
				now.monthday += 1
			}

		//months with 30 days
		case 4, 6, 9, 11:
			if now.monthday == 30 {
				now.monthday = 1
				now.month += 1
			} else {
				now.monthday += 1
			}
		// if it is February
		case 2:
			if now.year%400 == 0 {
				if now.monthday == 29 {
					now.monthday = 1
					now.month += 1
				} else {
					now.monthday += 1
				}
			} else if now.year%100 == 0 {
				if now.monthday == 28 {
					now.monthday = 1
					now.month += 1
				} else {
					now.monthday += 1
				}
			} else if now.year%4 == 0 {
				if now.monthday == 29 {
					now.monthday = 1
					now.month += 1
				} else {
					now.monthday += 1
				}
			} else {
				if now.monthday != 28 {
					now.monthday = 1
					now.month += 1
				} else {
					now.monthday += 1
				}
			}
		// if the month is December
		case 12:
			if now.monthday == 31 {
				now.monthday = 1
				now.month = 1
				now.year += 1
			} else {
				now.monthday += 1
			}
		}
		Today := DateStruct{day: now.day, monthday: now.monthday, month: now.month, year: now.year}
		calender = append(calender, Today)
		now = Today
		if now.year == 2000 && now.month == 12 && now.monthday == 31 {
			break
		}
		i += 1
		if i > 40000 {
			fmt.Println("Forceful break of the loop!")
			break
		}
	}

	fmt.Println("Total days: ", len(calender), " and i: ", i)
	// Looping through calender to count the number of required days.
	reqDays := 0
	for _, date := range calender {
		if date.day == 1 && date.monthday == 1 {
			reqDays += 1
			//fmt.Println("This day: ", date)
		}
	}
	fmt.Println("Number of days with Sunday on the first day of the month: ", reqDays)
	elapsed := time.Since(start)
	fmt.Println("Total time of run: ", elapsed)

}
