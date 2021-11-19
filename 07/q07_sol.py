class intcode:
    num_ls = []
    loc = 0
    mode = 0
    def __init__(self, mode):
        self.num_ls = [int(nm) for nm in open("q07_inp.txt", "r").read().split(',')]
        self.mode = mode

    def action(self, inp, res):
        while self.loc != -1:
            opc_full = self.num_ls[self.loc]
            code_2d = opc_full % 100
            if code_2d == 99:
                self.loc = -1
            elif code_2d == 4:
                res = self.num_ls[self.num_ls[self.loc + 1]]
                self.loc = self.loc + 2
                if self.mode != 0:
                    return res
            elif code_2d == 3:
                self.num_ls[self.num_ls[self.loc + 1]] = inp if self.loc == 0 else res
                self.loc = self.loc + 2    
            else:
                opc_full = str(opc_full).zfill(5)
                modes = str(int(opc_full) // 100).zfill(3)
                v1 = self.num_ls[self.loc + 1] if modes[2] == '1' else self.num_ls[self.num_ls[self.loc + 1]]
                v2 = self.num_ls[self.loc + 2] if modes[1] == '1' else self.num_ls[self.num_ls[self.loc + 2]]
                if code_2d == 5:
                    self.loc = v2 if v1 != 0 else self.loc + 3
                elif code_2d == 6:
                    self.loc = v2 if v1 == 0 else self.loc + 3
                elif code_2d in [1, 2]:
                    res1 = v1 + v2 if code_2d == 1 else v1 * v2
                else:
                    if code_2d == 7:
                        res1 = 1 if v1 < v2 else 0
                    else:
                        res1 = 1 if v1 == v2 else 0
                if code_2d in [1, 2, 7, 8]:
                    if modes[0] == '1':
                        self.num_ls[self.loc + 3] = res1  
                    else:
                        self.num_ls[self.num_ls[self.loc + 3]] = res1
                    self.loc = self.loc + 4
        return res
 
import itertools
 
lists = list(itertools.permutations([0,1,2,3,4]))
mx_pt_a = -1
obj = intcode(0)
for i in lists:
    val = 0
    for j in i:
        obj.loc = 0
        res = obj.action(j, val)
        val = res
    if val > mx_pt_a:
        mx_pt_a = val
print("Part A:", mx_pt_a)

lists = list(itertools.permutations([5,6,7,8,9]))
mx_pt_b = -1
for i in lists:
    val = 0
    objs = list(intcode(1) for i in range(0,5))
    mch, val = 0, 0
    while True:
        if objs[4].loc == -1:
            break
        else:
            res = objs[mch].action(i[mch], val)
            val = res
            mch = (mch + 1) % 5
    if val > mx_pt_b:
        mx_pt_b = val
    del objs
print("Part B:", mx_pt_b)