import math

def Fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        fib_num = Fibonacci(n-1) + Fibonacci(n-2)
        return fib_num


def list_of_Fib():
    fib_list = []
    for i in range(2,nterms+2):
        fib_num = Fibonacci(i)
        fib_list.append(fib_num)
    return fib_list

nterms = 10000

list = list_of_Fib()
print(max(list))


