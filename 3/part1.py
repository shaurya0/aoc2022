with open('1.txt', 'r') as fid:
    lines = fid.readlines()


a = ord('a')
A = ord('A')
priorities = {chr(a + i):(i+1) for i in range(0, 26)}
priorities.update({chr(A + i):(i+1+26) for i in range(0, 26)})
score = 0
for line in lines:
    l = line.strip()
    compartment1, compartment2 = set(l[:len(l)//2]), set(l[len(l)//2:])

    common = compartment1.intersection(compartment2)
    for c in common:
        score += priorities[c]


print(score)
