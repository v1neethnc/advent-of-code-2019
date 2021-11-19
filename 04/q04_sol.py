part_a, part_b = 0, 0
for num in range(197487, 673251 + 1):
    if len(set(str(num))) != len(list(str(num))) and sorted(str(num)) == list(str(num)):
        part_a += 1
        if 2 in [str(num).count(i) for i in set(str(num))]:
            part_b += 1
print("Part A:", part_a)
print("Part B:", part_b)