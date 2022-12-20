# %%
with open('1.txt', 'r') as fid:
    lines = fid.read().splitlines()



line = lines[0]
for i in range(len(line)-4):
    chunk = line[i:i+4]
    if len(set(chunk)) == 4:
        print(i+4)
        break
