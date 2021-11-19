def action(loc, inp):
    opc_full = num_ls[loc]
    code_2d = opc_full % 100
    if code_2d == 99: 
        return -1
    elif code_2d == 4:
        if (inp == 1 and num_ls[num_ls[loc + 1]] not in [0,3]) or inp == 5:
            print("Value:", num_ls[num_ls[loc + 1]])
        return loc + 2
    elif code_2d == 3:
        num_ls[num_ls[loc + 1]] = inp
        return loc + 2        
    else:
        opc_full = str(opc_full).zfill(5)
        modes = str(int(opc_full) // 100).zfill(3)
        v1 = num_ls[loc + 1] if modes[2] == '1' else num_ls[num_ls[loc + 1]]
        v2 = num_ls[loc + 2] if modes[1] == '1' else num_ls[num_ls[loc + 2]]
        if code_2d == 5:
            return v2 if v1 != 0 else loc + 3
        elif code_2d == 6:
            return v2 if v1 == 0 else loc + 3
        elif code_2d in [1, 2]: 
            res = v1 + v2 if code_2d == 1 else v1 * v2
        else:
            if code_2d == 7:
                res = 1 if v1 < v2 else 0
            else:
                res = 1 if v1 == v2 else 0
        if modes[0] == '1':
            num_ls[loc + 3] = res  
        else: 
            num_ls[num_ls[loc + 3]] = res
        return loc + 4
    
for inp in [1, 5]:
    num_ls = [int(nm) for nm in open("q05_inp.txt", "r").read().split(',')]
    loc = 0
    while loc != -1:
        loc = action(loc, inp)