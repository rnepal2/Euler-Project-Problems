import math

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        fib_num = fibonacci(n-1) + fibonacci(n-2)
        return fib_num


def list_of_fib():
    fib_list = []
    for i in range(2,nterms+2):
        fib_num = fibonacci(i)
        fib_list.append(fib_num)
    return fib_list

nterms = 10000

list = list_of_fib()
print(max(list))


