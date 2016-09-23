import math
import time

start_time = time.time()

def Check_Prime(N):
		if all(N % i != 0 for i in range(2,N)):
			return True
		return False
		
def List_Primes(n):
	prime_list = []
	for i in range(2,n):
		if Check_Prime(i) == True:
			prime_list.append(i)
	return prime_list
		
def Sum_Of_Primes(a_list):
	sum = 0
	for i in a_list:
		sum = sum + i
	return sum 
	
	
num = int(input("Enter a number upto which prime is to listed: "))
#ans = List_Primes(num)
#length = len(ans)
#total_sum = Sum_Of_Primes(ans)
#print("The required sum is: ", total_sum)

print(Check_Prime(num))

print("The run time is: ", time.time() - start_time)
