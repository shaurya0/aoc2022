with open('1.txt', 'r') as fid:
    lines = fid.read().splitlines()

# %%
stacks = [[] for _ in range(9)]
for i in reversed(range(8)):
    line = lines[i]
    n = 4
    s = [line[i:i+n] for i in range(0, len(line), n)]
    for ii,c in enumerate(s):
        if c[0] =='[':
            stacks[ii].append(c[1])


for i in range(10, len(lines)):
    l = lines[i].split(' ')
    num = int(l[1])
    source = int(l[3]) - 1
    dest = int(l[5]) - 1


    vals = stacks[source][-num:]
    stacks[dest].extend(vals)
    stacks[source] = stacks[source][:-num]


output = ''
for s in stacks:
    output +=s[-1]
