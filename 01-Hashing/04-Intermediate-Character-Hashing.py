s = 'azyxyyzZAABaaaAa'
q = ['d', 'a', 'y', 'x', 'A', 'B', 'Z']
hash_list = [0] * 58

for ch in s:
    ascii_value = ord(ch)
    index = ascii_value - 65
    hash_list[index] += 1

print(hash_list)

for ch in q:
    ascii_value = ord(ch)
    index = ascii_value - 65
    print(f"{ch}:{hash_list[index]}")