# %%
import numpy as np
import math

elevation = []
sources = []
with open('1.txt') as f:
    lines = [l.strip().split(' ') for l in f.readlines()]
    for i,line in enumerate(lines):
        row = []
        for j,c in enumerate(line[0]):
            char = c
            if c == 'S' or c == 'a':
                sources.append((i,j))
                char = 'a'
            if c == 'E':
                dest = i,j
                char = 'z'

            row.append(abs(ord(char) - ord('z')))

        elevation.append(row)

elevation = np.array(elevation)
ROWS,COLS = elevation.shape
sources = [s[0]*COLS + s[1] for s in sources]
dest = dest[0]*COLS + dest[1]

# %%
adjacency_list = []
for i in range(ROWS):
    for j in range(COLS):
        adjacencies = []

        cur = elevation[i,j]
        if i != 0:
            up = elevation[i-1,j]
            node = (i-1)*COLS + j
            if up == cur + 1 or up <= cur:
                adjacencies.append((node, 1))
                # adjacencies.append((node, up))
        if i != (ROWS-1):
            down = elevation[i+1,j]
            node = (i+1)*COLS + j
            if down == cur + 1 or down <= cur:
                adjacencies.append((node, 1))
                # adjacencies.append((node, down))
        if j != 0:
            left = elevation[i,j-1]
            node = (i)*COLS + j-1
            if left == cur + 1 or left <= cur:
                adjacencies.append((node, 1))
                # adjacencies.append((node, left))
        if j != (COLS -1):
            node = (i)*COLS + j+1
            right = elevation[i,j+1]
            if right == cur + 1 or right <= cur:
                adjacencies.append((node, 1))
                # adjacencies.append((node, right))

        adjacency_list.append(adjacencies)

# %%

#  1  function Dijkstra(Graph, source):
#  2
#  3      for each vertex v in Graph.Vertices:
#  4          dist[v] ← INFINITY
#  5          prev[v] ← UNDEFINED
#  6          add v to Q
#  7      dist[source] ← 0
#  8
#  9      while Q is not empty:
# 10          u ← vertex in Q with min dist[u]
# 11          remove u from Q
# 12
# 13          for each neighbor v of u still in Q:
# 14              alt ← dist[u] + Graph.Edges(u, v)
# 15              if alt < dist[v]:
# 16                  dist[v] ← alt
# 17                  prev[v] ← u
# 18
# 19      return dist[], prev[]


# %%
def dijkstra(source):
    dist = list()
    prev = list()
    queue = list()
    for ii in range(ROWS*COLS):
        dist.append(np.iinfo(np.uint64).max)
        prev.append(None)
        queue.append(ii)

    dist[source] = 0
    dist = np.array(dist, dtype=np.uint64)

    while len(queue) > 0:
        min_dist = math.inf
        for q in queue:
            if dist[q] < min_dist:
                min_dist = dist[q]
                u = q

        queue.remove(u)

        neighbors = adjacency_list[u]
        neighbors = [n for n in neighbors if n[0] in queue]

        for n in neighbors:
            v, neighbor_dist = n
            alt = dist[u] + neighbor_dist
            if alt < dist[v]:
                dist[v] = alt
                prev[v] = u

    return prev

path = dijkstra(dest)
path = np.array(path)

for np in np.where(path==None)[0]:
    if np in sources:
        sources.remove(np)

# %%
min_steps = math.inf
for s in sources:
    prev = s
    steps = 0
    while True:
        n = path[prev]
        if n is None:
            break
        steps += 1
        prev = n

    if steps < min_steps:
        min_steps = steps


