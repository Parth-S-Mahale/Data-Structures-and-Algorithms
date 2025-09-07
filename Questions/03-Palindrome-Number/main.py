num = 1221
def ispalindrome(num):
    if num < 0:
        return False

    original = num
    reverse = 0

    while num > 0:
        reverse = reverse * 10 + num % 10
        num = num // 10
    return f"{original == reverse}"

print(ispalindrome(num))
