with open('1.txt', 'r') as fid:
    lines = fid.read().splitlines()



# |--------|
#        |--------|

# |--------|
#   |---|

# |--------|
# |--------|




count = 0
for l in lines:
    a1, a2 = l.split(',')

    a1_start, a1_end = [int(x) for x in a1.split('-')]
    a2_start, a2_end = [int(x) for x in a2.split('-')]
    a1_size = a1_end - a1_start
    a2_size = a2_end - a2_start

    a1_set = set(range(a1_start, a1_end+1))
    a2_set = set(range(a2_start, a2_end+1))
    if len(a1_set.intersection(a2_set)) > 0:
        count += 1

print(count)
