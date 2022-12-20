# %%
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

# Do while
instr, cycles_left, val = parse_line(lines[ll])

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

    if cycle == 20 or cycle == 60 or cycle == 100 or cycle == 140 or cycle == 180 or cycle == 220:
        print(f'cycle: {cycle}, X: {X}')
        total_sum += cycle*X


    # print(f"Cycle: {cycle}, X: {X}, instr: {instr}, val: {val}")



    cycle += 1
    cycles_left -= 1

print(total_sum)
# print(f"Cycle: {cycle}, X: {X}, instr: {instr}, val: {val}")
