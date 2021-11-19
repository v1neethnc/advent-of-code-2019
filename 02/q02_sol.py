def result_calc(num_lst):
    st_index = 0
    while num_ls[st_index] != 99:
        num1, num2 = num_lst[num_lst[st_index + 1]], num_lst[num_lst[st_index + 2]]
        res = num1 + num2 if num_lst[st_index] == 1 else num1 * num2
        num_lst[num_lst[st_index + 3]] = res
        st_index += 4
    return num_lst[0]

num_ls = [int(nm) for nm in open("q02_inp.txt", "r").read().split(',')]
for i in range(0, 100):
    for j in range(0, 100):
        st_index = 0
        temp_list = [element for element in num_ls]
        temp_list[1], temp_list[2] = i, j
        res = result_calc(temp_list)
        if i == 12 and j == 2:
            print("Part A:", res)
        if res == 19690720:
            print("Part B:", 100 * i + j)