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

def visible(direction, value):
    if direction.shape[0] == 0:
        return 0

    boundary = np.argmax(direction>=value)
    if boundary == 0:
        if direction[0] == value:
            num_visible = 1
        elif direction[0] > value:
            num_visible = 0

        # all the way to the edge
        else:
            num_visible = len(direction)
    else:
        num_visible = boundary + 1

    return num_visible





max_visible = 0
for i in range(N):
    for j in range(N):
        t = grid[i,j]
        # check for edge
        # np.argmax(top >= t) + 1
        top = grid[0:i,j]
        top = top[::-1]
        bottom = grid[i+1:,j]
        left = grid[i,0:j]
        left = left[::-1]
        right = grid[i,j+1:]

        num_visible = visible(top, t) * visible(bottom, t) * visible(left, t) * visible(right, t)
        if num_visible > max_visible:
            max_visible = num_visible

print(max_visible)
