import math
import time
from functools import reduce

start_time = time.time()


def Num_Of_Factors(n):    
	factors_list = set(reduce(list.__add__,([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))
	return len(factors_list)


def List_To_Check(n):
	list_of_numbers = []
	for i in range(1000000, n):
		list_of_numbers.append(i)
	return list_of_numbers
	
def Num_With_MaxFactors(a_list):
	factors = []
	for i in a_list:
		factors.append(Num_Of_Factors(i))
	return max(factors)
		
	


check_upto = int(input("Enter the number to check upto: "))
list_of_nums = List_To_Check(check_upto)
sorted_list = sorted(list_of_nums)
ans = Num_With_MaxFactors(sorted_list)
print("The maxmum number of factors are: ",ans)


print(2**500500)





	
print("The total run time is: ", time.time() - start_time)