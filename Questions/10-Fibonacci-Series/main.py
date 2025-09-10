num = int(input("Enter a number"))

def func(num):  
    if num == 0 or num == 1:
        return num
    return func(num-1) + func(num-2)

print(func(num))