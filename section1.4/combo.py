"""
ID: ashayp21
LANG: PYTHON3
TASK: combo
"""
fin = open ('combo.in', 'r')
fout = open ('combo.out', 'w')

vals = fin.read().splitlines() #gets every line

N = int(vals[0])

combo1 = list(map(int, vals[1].split(" ")))
combo2 = list(map(int, vals[2].split(" ")))

all_combos = []

def converted(n):
    if n <= 0:
        return converted(N + n)
    elif n > N:
        return converted(n - N)
    return n

for i in range(-2, 3):
    for j in range(-2, 3):
        for z in range(-2, 3):
            all_combos.append(str(converted(i+combo1[0])) + "," + str(converted(j+combo1[1])) + "," +
                              (str(converted(z+combo1[2]))))

for i in range(-2, 3):
    for j in range(-2, 3):
        for z in range(-2, 3):
            all_combos.append(str(converted(i + combo2[0])) + "," + str(converted(j + combo2[1])) + "," +
                              (str(converted(z + combo2[2]))))


all_combos = list( dict.fromkeys(all_combos) )

fout.write(str(len(all_combos)) + "\n")