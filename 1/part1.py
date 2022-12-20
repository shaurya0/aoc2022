# %%
f = '1.txt'

with open(f, 'r') as fid:
    calories = fid.readlines()

elf = 1
max_cals = 0
max_elf = 1
cals = 0
for cal in calories:
    if cal == '\n':
        if cals > max_cals:
            max_cals = cals
            max_elf = elf


        elf += 1
        cals = 0
        continue

    cals += int(cal.strip())


print(max_cals)

