with open('1.txt', 'r') as fid:
    lines = fid.readlines()

score = 0
#X lose
#Y draw
#Z win
for line in lines:
    if line[0] == 'A':
        if line[2] == 'X':
            score += 3
        if line[2] == 'Y':
            score += 4
        if line[2] == 'Z':
            score += 8
    if line[0] == 'B':
        if line[2] == 'X':
            score += 1
        if line[2] == 'Y':
            score += 5
        if line[2] == 'Z':
            score += 9
    if line[0] == 'C':
        if line[2] == 'X':
            score += 2
        if line[2] == 'Y':
            score += 6
        if line[2] == 'Z':
            score += 7


print(score)



