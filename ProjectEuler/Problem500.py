import math
import time
from functools import reduce

start_time = time.time()


def num_of_factors(n):    
	factors_list = set(reduce(list.__add__,([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))
	return len(factors_list)


def list_to_check(n):
	list_of_numbers = []
	for i in range(1000000, n):
		list_of_numbers.append(i)
	return list_of_numbers
	
def num_with_maxfactors(a_list):
	factors = []
	for i in a_list:
		factors.append(num_of_factors(i))
	return max(factors)
		
	


check_upto = int(input("Enter the number to check upto: "))
list_of_nums = list_to_check(check_upto)
sorted_list = sorted(list_of_nums)
ans = num_with_maxfactors(sorted_list)
print("The maxmum number of factors are: ",ans)

print("The total run time is: ", time.time() - start_time)
