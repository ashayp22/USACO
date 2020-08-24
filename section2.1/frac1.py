"""
ID: ashayp21
LANG: PYTHON3
TASK: frac1
"""
fin = open ('frac1.in', 'r')
fout = open ('frac1.out', 'w')

vals = fin.read().splitlines() #gets every line
N = int(vals[0])

def euler(a, b):
    if b == 0:
        return a
    return euler(b, a % b)



def reduceFraction(x, y):
    d = euler(x, y)

    x = x // d
    y = y // d

    return (x,y)


s = set()

for i in range(N, 0, -1):
    for j in range(0, i+1):
        s.add(reduceFraction(j, i))

s.add((0, 1))
s.add((1, 1))

s = list(s)

print(s)

arr = sorted(s, key=lambda x: x[0] / x[1])

ans = ""

for a in arr:
    ans += str(a[0]) + "/" + str(a[1]) + "\n"

fout.write(ans)


