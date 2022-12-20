# %%
import numpy as np

lines = []
with open('1.txt', 'r') as fid:
    lines_ = fid.read().splitlines()

for l in lines_:
    x = [int(c) for c in l]
    lines.append(np.array(x))

grid = np.array(lines)
N = grid.shape[0]

visible = 2*N + 2*(N-2)
for i in range(1, N-1):
    for j in range(1, N-1):
        t = grid[i,j]
        top = grid[0:i,j]
        bottom = grid[i+1:,j]
        left = grid[i,0:j]
        right = grid[i,j+1:]

        if any([all(t > top) or all(t>bottom) or all(t>left) or all(t>right)]):
            visible += 1

print(visible)
