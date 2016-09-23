# Largest Prime Factor of a Number

import math
import os
import time

start_time = time.time()

start_search_from = int(5e11)
def Any_Factors(n):
    list_to_search = []
    for i in range(1, n):
        if i % 2 == 0: continue
        if i % 3 == 0: continue
        if i % 5 == 0: continue
        if i % 7 == 0: continue
        if i % 11 == 0: continue
        if i % 17 == 0: continue
        list_to_search.append(i)

    list_factors = []
    for i in list_to_search:
        if n % i == 0:
            list_factors.append(i)
    return list_factors

# the_num = int(input("Enter the number: "))

given_num = 600851475143
# ans = Prime_Factors(the_num)
ans = Any_Factors(given_num)
print("The prime factors of the number are: ", ans)
print("The time taken is: ", time.time()- start_time)

