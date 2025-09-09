# sum of N to 1 --> Parameterized Recursion
def func(sum, i, N):
    if i > N:
        print(sum)
        return
    func(sum + i, i + 1, N)

func(0,1,4)