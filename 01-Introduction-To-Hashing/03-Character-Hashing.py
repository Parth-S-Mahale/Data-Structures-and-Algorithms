s = 'azyxyyzaaaa'
q = ['d', 'a', 'y', 'x']
hash_list = [0] * 26

for ch in s:
    ascii_value = ord(ch)
    index = ascii_value - 97
    hash_list[index] += 1

print(hash_list)

for ch in q:
    ascii_value = ord(ch)
    index = ascii_value - 97
    print(f"{ch}:{hash_list[index]}")