with open('1.txt', 'r') as fid:
    lines = fid.read().splitlines()

count = 0
for l in lines:
    a1, a2 = l.split(',')

    a1_start, a1_end = [int(x) for x in a1.split('-')]
    a2_start, a2_end = [int(x) for x in a2.split('-')]
    a1_size = a1_end - a1_start
    a2_size = a2_end - a2_start
    if a2_size >= a1_size:
        if a2_start <= a1_start and a2_end >= a1_end:
            count += 1
    else:
        if a1_start <= a2_start and a1_end >= a2_end:
            count += 1

print(count)
