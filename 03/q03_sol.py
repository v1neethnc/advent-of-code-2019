l_nm = 1
line1_pts_steps = {}
line2_pts_steps = {}
with open('q03_inp.txt', 'r') as file:
    for line in file.readlines():
        x_coord, y_coord = 0, 0
        step_count = 1
        data = line.replace('\n', '')
        data = data.split(",")
        for i in data:
            for j in range(0, int(i[1:])):
                if i[0] == 'U':
                    y_coord += 1
                elif i[0] == 'D':
                    y_coord -= 1
                elif i[0] == 'R':
                    x_coord += 1
                elif i[0] == 'L':
                    x_coord -= 1
                if l_nm == 1:
                    line1_pts_steps[step_count] = (x_coord, y_coord)
                else:
                    line2_pts_steps[step_count] = (x_coord, y_coord)
                step_count += 1
        l_nm += 1
    line1_pts = set(val for val in line1_pts_steps.values())
    line2_pts = set(val for val in line2_pts_steps.values())
    intersections = [(x,y) for (x,y) in line1_pts.intersection(line2_pts)]
    part_a_res = min([x+y for (x,y) in intersections if x >= 0 and y >= 0])
    print("Part A:", part_a_res)
    res_1 = [(line1_pts_steps[x], x) for x in line1_pts_steps.keys() if line1_pts_steps[x] in intersections]
    res_2 = [(line2_pts_steps[x], x) for x in line2_pts_steps.keys() if line2_pts_steps[x] in intersections]
    res_final = [x[1] + y[1] for x in res_1 for y in res_2 if x[0] == y[0]]
    print("Part B:", min(res_final))