"""
ID: ashayp21
LANG: PYTHON3
TASK: crypt1
"""
fin = open ('crypt1.in', 'r')
fout = open ('crypt1.out', 'w')

vals = fin.read().splitlines() #gets every line

num_digits = int(vals[0])
numbers = list(map(int, vals[1].split(" ")))

num_solutions = 0

def checkValid(line, length):
    split = list(line)

    if len(split) != length:
        return False

    for s in split:
        if int(s) not in numbers:
            return False
    return True

print(numbers)

for a in numbers:
    for b in numbers:
        for c in numbers:
            for d in numbers:
                for e in numbers:
                    abc = (a*100)+(b*10)+c
                    if checkValid(str(e * abc), 3):
                        if checkValid(str(d * abc), 3):
                            if checkValid(str((d*10 + e)*abc), 4):
                                num_solutions += 1

fout.write (str(num_solutions) + "\n")
