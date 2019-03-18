import math
import time 


def is_prime(num):
    num = abs(num)
    # returns a bool: True if the number n is prime, else False
    if num == 2 or num == 3 or num == 5:
        return True
    if num % 2 == 0 or num % 3 == 0 or num % 5 == 0:
        return False
    for i in range(2, int(math.sqrt(num)+1)):
        if num % i == 0:
            return False 
    return True


# returns the quadratic value
def quadratic_value(n, a, b):
    return n*n + a*n + b


start_time = time.time()


n = 75
nmax, req_a, req_b = 0, 0, 0
for a in range(-1000, 1000):
    for b in range(-1000, 1000):
        for i in range(n):
            quad_value = quadratic_value(i, a, b)
            if is_prime(quad_value) is False:
                req_a = a
                req_b = b
                break
        # if nmax is greater than previous: update values
        if i > nmax:
            nmax = i
            req_values = [nmax, req_a, req_b]


print("nmax: ", req_values)
print("Required product is: ", req_values[1]*req_values[2])
print("Total time taken: ", time.time() - start_time)



