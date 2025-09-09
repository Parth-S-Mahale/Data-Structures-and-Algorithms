s = "ABC6E6CBA"
left = 0
right = len(s)-1

def stringIsPalindrome(s, left, right):
    if left >= right:
        return True
    if s[left] != s[right]:
        return False
    
    return stringIsPalindrome(s, left+1, right-1)


print(stringIsPalindrome(s, left, right))
 