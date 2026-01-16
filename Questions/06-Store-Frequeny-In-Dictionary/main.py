num_list = [5, 6, 7, 7, 1, 9, 111, 1, 1, 5, 1, 1]
freq_map = {}

# Better Approach:
""" for i in range(0, len(num_list)):
    if num_list[i] in freq_map:
        freq_map[num_list[i]] += 1
    else:
        freq_map[num_list[i]] = 1
        
print(freq_map) """

#Optimal Approach:
for i in range(0, len(num_list)):
    freq_map[num_list[i]] = freq_map.get(num_list[i], 0) + 1
    
print(freq_map)