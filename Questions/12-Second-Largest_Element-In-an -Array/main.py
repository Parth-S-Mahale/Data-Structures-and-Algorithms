n = 8
a = [3,5,6,7,8,9,10,20]

def getSecondOrderElements(n, a):
    
    smallest = second_smallest = float('inf')
    largest = second_largest = float('-inf')
    
    for num in a:
       
        if num < smallest:
            second_smallest = smallest
            smallest = num
        elif num < second_smallest:
            second_smallest = num
        
       
        if num > largest:
            second_largest = largest
            largest = num
        elif num > second_largest:
            second_largest = num
    
    return [second_largest, second_smallest]

print(getSecondOrderElements(n, a))