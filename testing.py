import numpy as np

with open('q08_inp.txt', 'r') as data:
    data = np.array(list(data.read().strip())).reshape((-1, 6, 25))

res, min_zeroes = 0, 150
for i in data:
    unique, counts = np.unique(i, return_counts=True)
    res_dict = dict(zip(unique, counts))
    if min_zeroes > res_dict['0']:
        min_zeroes = res_dict['0']
        res = res_dict['1'] * res_dict['2']
print(res)

final_img = data[0]
for i in data:
    final_img = np.where(final_img != '2', final_img, i)


final_img = np.where(final_img == '0', " ", "|")
for i in final_img:
    for j in i:
        print(j, end = '')
    print()