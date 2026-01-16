# 1 To N --> Tail Recursion
def func(N):
    if N == 0:
        return
    
    func(N-1)
    print(N)

func(4)