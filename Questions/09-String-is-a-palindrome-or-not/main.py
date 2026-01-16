s = "ABCDEDCBA"
left = 0
right = len(s)-1

def stringIsPalindrome(s, left, right):
    while left < right:
        if s[left] != s[right]:
            return False
        
        left += 1
        right -= 1
    
    return True

print(stringIsPalindrome(s, left, right))
 