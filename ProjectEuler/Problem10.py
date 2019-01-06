import math
import time

start_time = time.time()

def check_prime(N):
		if all(N % i != 0 for i in range(2,N)):
			return True
		return False
		
def list_primes(n):
	prime_list = []
	for i in range(2,n):
		if check_prime(i) == True:
			prime_list.append(i)
	return prime_list
		
def sum_of_primes(a_list):
	sum = 0
	for i in a_list:
		sum = sum + i
	return sum 
	
	
num = int(input("Enter a number upto which prime is to listed: "))
ans = list_primes(num)
length = len(ans)
total_sum = sum_of_primes(ans)
print("The required sum is: ", total_sum)
print(check_prime(num))
print("The run time is: ", time.time() - start_time)
