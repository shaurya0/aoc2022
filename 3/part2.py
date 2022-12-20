with open('1.txt', 'r') as fid:
    lines = fid.read().splitlines()


a = ord('a')
A = ord('A')
priorities = {chr(a + i):(i+1) for i in range(0, 26)}
priorities.update({chr(A + i):(i+1+26) for i in range(0, 26)})
score = 0
for e1, e2, e3 in zip(*[iter(lines)]*3):
    e1,e2,e3 = set(e1), set(e2), set(e3)
    common = e1.intersection(e2).intersection(e3)
    for c in common:
        score += priorities[c]

print(score)
