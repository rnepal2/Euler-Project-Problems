
import math
import time

# sum of the multiples of 3 or 5 below 1000
def sum_of_multiples():
    total_sum = 0
    for i in range(1000):
        if (i % 3 == 0) | (i % 5 == 0):
            total_sum += i
    return total_sum

start_time = time.time()
print("The sum of the multiples of 3 or 5 below 1000 is: = ", sum_of_multiples())
print("Time taken: ", time.time() - start_time)


