# Largest Prime Factor of a Number

import math
import os
import time

start_time = time.time()

def factorial(n):
	if n <= 1: return 1
	else: 
		return n*factorial(n-1)

def sum_of_digits(n):
	fact_of_n = factorial(n)
	string_n = str(fact_of_n)
	
	list_of_digits = []
	for i in string_n:
		list_of_digits.append(i)
	new_list = list_of_digits
	
	int_list = []             # remove this for loop just by converting i into string in above for loop int(i)
	for j in new_list:
		int_list.append(int(j))		
	final_list = int_list
	
	sum = 0
	for k in final_list:
		sum += k
	return sum
	
n = int(input("Enter a number: "))
ans = sum_of_digits(n)
print("The factorial of the number is: ", ans)
		
print("The time taken is: ", time.time()- start_time)

