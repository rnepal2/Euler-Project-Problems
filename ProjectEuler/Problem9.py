#Special Pythagorean Triplet

import math
import time

start_time = time.time()

def List_Pythagorean():
	list_pairs = []
	for i in range(1,426):
		for j in range(i+1,426):
			for k in range(j+1,426):
				if (i**2 + j**2 == k**2)and(i + j + k == 1000):
					return [i, j, k]
	
    
ans = List_Pythagorean()
print("\nThe required Pythagorean triplet is: ", ans)

#print("Check if the triplet is pythagorean")
the_product = ans[0]*ans[1]*ans[2]
print("The product of the Pythagorean triplet elements is: ", the_product)
					
print("The total run time is: ", time.time()- start_time)

#print("The number is: ", the_num)

