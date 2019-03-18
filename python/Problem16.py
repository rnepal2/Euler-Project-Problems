import math
import time

start_time = time.time()

the_num = 2**1000
num_string = str(the_num)
length = len(num_string)

def list_of_digits(some_list):
	list_digits = []
	for i in some_list:
		integer_i = int(i)
		list_digits.append(integer_i)
	return list_digits
	
def sum_of_digits(digits_list):
	sum = 0
	for i in digits_list:
		sum += i
	return sum
	
digits_list = list_of_digits(num_string)	
ans = sum_of_digits(digits_list)
print("\nThe summation of the digits in the number is: ", ans)

print("The total run time is: ", time.time()- start_time)

#print("The number is: ", the_num)