# Maximum Digital Sum

import math
import os
import time

start_time = time.time()

def Power_Numbers(a, b):
	list_numbers = []
	for i in range(1, a):
		for j in range(1, b):
			list_numbers.append(i**j)
	return list_numbers

def Sum_Of_Digits(a_num):
	string_n = str(a_num)
	
	list_of_digits = []
	for i in string_n:
		list_of_digits.append(int(i))
	new_list = list_of_digits
	
	sum = 0
	for k in new_list:
		sum += k
	return sum
	
def Greatest_Sumof_Digits(a_list):
	list_of_sum = []
	for i in a_list:
		sum = Sum_Of_Digits(i)
		list_of_sum.append(sum)
	
	max_sum = max(list_of_sum)
	return max_sum
		

	
list_all = Power_Numbers(100, 100)
ans = Greatest_Sumof_Digits(list_all)
print("The maximum digital sum is: ", ans)

print("The time taken is: ", time.time()- start_time)

