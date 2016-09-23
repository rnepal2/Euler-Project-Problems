# Largest Prime Factor of a Number

import math
import os
import time

start_time = time.time()

def Find_rmax(_a,n):
	list_of_r = []
	a = _a
	for i in range(0,n+1):
		r = ((a - 1)**i + (a + 1)**i) % (a**2)
		list_of_r.append(r)
	#print(max(list_of_r))
	return max(list_of_r)
	
def Sum_Of_rmax(n):
	rmax_sum = 0
	_N = n
	for i in range(3,1001):
		rmax_sum += Find_rmax(i,_N)
	return rmax_sum
	

n = int(input("\nEnter a number: "))
ans = Sum_Of_rmax(n)

print("\nThe sum of r_max is: ", ans)
		
print("\nThe time taken is: ", time.time()- start_time)

