# %%
with open('1.txt', 'r') as fid:
    lines = fid.read().splitlines()



line = lines[0]
for i in range(len(line)-14):
    chunk = line[i:i+14]
    if len(set(chunk)) == 14:
        print(i+14)
        break
