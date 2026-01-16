from math import sqrt
num = 15
result = []

# BruteForce Approach:
""" def factors(num):
    for i in range(1,num+1):
        if num % i == 0:
            result.append(i)
    return result

print(factors(num)) """

# Better Approach:
""" def factors(num):
    for i in range(1,num//2):
        if num % i == 0:
            result.append(i)
    result.append(num)
    return result

print(factors(num)) """

# Optimal Approach:
def factors(num):
    for i in range(1,int(sqrt(num))+1):
        if num % i == 0:
            result.append(i)
            if num // i != i:
                result.append(num // i)
    result.sort()
    return result

print(factors(num))


