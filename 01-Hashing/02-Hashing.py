n = [5, 3, 2, 2, 1, 5, 5, 7, 5, 10]
m = [10, 111, 1, 9, 5, 67, 2]
freq_map = {}
# print(len(n))

for i in range(0, len(n)):
    if n[i] in freq_map:
        freq_map[n[i]] += 1
    else:
        freq_map[n[i]] = 1
        
print(freq_map)

for i in range(0, len(m)):
    if m[i] in freq_map:
        print(f"{m[i]}:{freq_map[m[i]]}")
    else:
        print(f"{m[i]}:{0}")