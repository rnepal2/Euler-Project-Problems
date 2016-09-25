import math
import time

start_time = time.time()

		
def List_Primes(from_n, to_n):
	from_n = int(from_n/2 * 2 + 1)
	lNum = range(from_n, to_n + 1, 2)
	i_root = to_n ** 0.5
	i_mid = len(lNum)
	i = 0
	m = 3

	while m < i_root:
		j = (m*m - from_n)/2
		while j < i_mid:
			if j >= 0:	
				lNum[j] = 0
			j += m
		i += 2
		m += 2

	return [x for x in lNum if x != 0]



	
	
from_n = int(input("Enter a number upto which prime is to listed: "))

to_n = int(input("Enter the upper limit: "))

list_prime = List_Primes(from_n, to_n)

print("The list of prime numbers is: ", list_prime)

print("The total run time is: ", time.time() - start_time)
