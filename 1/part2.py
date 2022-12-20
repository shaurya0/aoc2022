# %%
f = '1.txt'
import heapq

with open(f, 'r') as fid:
    calories = fid.readlines()

elf = 1
cals = 0
elf_cals = []
for cal in calories:
    if cal == '\n':
        heapq.heappush(elf_cals, -cals)

        cals = 0
        continue

    cals += int(cal.strip())

print(abs(elf_cals[0] + elf_cals[1] + elf_cals[2]))
