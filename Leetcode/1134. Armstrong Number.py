n = 153
nod = len(str(n))
total = 0

while n > 0:
    total = total + (n % 10) ** nod
    n //= 10

print(total)