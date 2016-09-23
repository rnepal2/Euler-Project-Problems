import math

def list_all_multiples(N):
    init_list = []
    for i in range(1, N):
        if (i % 3 == 0)or(i % 5 == 0):
            init_list.append(i)
    return(init_list)

    #print(init_list)

def Sum_of_multiples():
    req_list = list_all_multiples(1000)
    n = len(req_list)
    #print(n)
    total_sum = 0
    for i in req_list:
        total_sum += i
    return total_sum

print("The sum of the multiples of 3 and 5 upt0 1000 is: = ", Sum_of_multiples())




