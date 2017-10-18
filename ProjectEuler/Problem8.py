import math
import time

# loading the number from the file
with open("1000-digit-number.txt") as f:
    lines = []
    for line in f:
        lines.append(line)
lines = [line.rstrip('\n') for line in lines]
number = ''.join(lines) # as a string

start_time = time.time()

max_product = 1
for start in range(len(number) - 13):
    product = 1
    for i in range(start, start + 13):
        product *= int(number[i])
    if product > max_product:
        max_product = product
        
print("Maximum consecutive 13 numbers is: ", max_product)
print("Total run time: ", time.time() - start_time)