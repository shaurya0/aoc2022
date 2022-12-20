# %%
import numpy as np
with open('1.txt') as f:
    lines = [l.strip().split(' ') for l in f.readlines()]

add_cycles = 2
noop_cycles = 1

def parse_line(line):
    if len(line) > 1: # addx
        instr, val = line[0], int(line[1])
        cycles_left = add_cycles
    else:
        instr = 'noop'
        cycles_left = noop_cycles
        val = None

    return instr, cycles_left, val


# %%
X = 1
ll = 0
cycle = 1


crt = [['.']*40 for _ in range(6)]
def print_crt(crt):
    ss =''
    for i in range(6):
        for j in range(40):
            ss += crt[i][j]

        ss += '\n'
    print(ss)

# Do while
instr, cycles_left, val = parse_line(lines[ll])
ii,jj = 0,0

total_sum = 0
while True:
    if cycles_left == 0:
        if instr == 'addx':
            X += val
        ll += 1
        if ll == len(lines):
            break
        line = lines[ll]

        instr, cycles_left, val = parse_line(line)


    y1,y2,y3 = X-1, X, X+1

    if jj == y1:
        crt[ii][jj] = '#'
    elif jj == y2:
        crt[ii][jj] = '#'
    elif jj == y3:
        crt[ii][jj] = '#'


    jj += 1
    if jj == 40:
        ii += 1
        jj = 0

    cycle += 1
    cycles_left -= 1


print_crt(crt)
