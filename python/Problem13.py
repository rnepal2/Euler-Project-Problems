import math
import time
import csv 

start_time = time.time()

def make_list():
	with open('TheNumbers.txt', 'rb') as csvfile:
		list_of_numbers = []
		for row in csvfile:
			numbers = row.split()
			list_of_numbers.append(int(numbers[0]))
		return list_of_numbers
		
def sum_of_numbers(a_list):
	sum = 0
	for i in a_list:
		sum += i
	return sum

		
the_list = make_list()
ans = sum_of_numbers(the_list)
sum_string = str(ans)
length = len(sum_string)

firs_ten_digits = sum_string[0:10]

print("The first ten digits of the sum of the numbers in the file is: ",firs_ten_digits)

#print("The sum of all numbers inside the data file is: ", ans)

print("The total run time is: ", time.time()- start_time)

#print("The number is: ", the_num)
