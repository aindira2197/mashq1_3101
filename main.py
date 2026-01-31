# 1
lst = list(range(1, 11))

# 2
letters = []
for ch in input():
    letters.append(ch)

# 3
numbers = [int(input())]

# 4
new_list = []
new_list.extend(lst)
new_list.extend(numbers)

# 5
empty = []
empty += [1, 2]
empty += [3, 4]
empty += [5, 6]

# 6
for ch in input():
    letters.append(ch)

# 7
odd = [1, 3, 5]
even = [2, 4, 6]
merged = []
merged.extend(odd)
merged.extend(even)
