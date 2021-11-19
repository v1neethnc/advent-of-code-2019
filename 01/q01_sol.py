def fuel_calc(value):
	return max((value//3) - 2, 0)

part_a_ans = 0
part_b_ans = 0
with open("q01_inp.txt", "r") as fp:
	for line in fp.readlines():
		part_a_ans += fuel_calc(int(line))
		while int(line) > 0:
			line = fuel_calc(int(line))
			part_b_ans += line

print("Part A:", part_a_ans)
print("Part B:", part_b_ans)