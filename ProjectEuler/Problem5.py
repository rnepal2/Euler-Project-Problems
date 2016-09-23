import math
import time

start_time = time.time()

def LCM(Num):
	i = 1
	while i <= Num + 1:
		that_num = []
		for j in range(1,11):
			if i % j == 0: 
			   that_num.append(i)
		return that_num  
	i += 1

ans = LCM(2520 )
print(ans)

print("The run time is: ", time.time() - start_time)


def multiply(num):
	ans = 1
	for i in range(1, num + 1):
		ans *= i
	return ans
	
print(multiply(10))