"""
ID: ashayp21
LANG: PYTHON3
TASK: wormhole
"""
fin = open ('wormhole.in', 'r')
fout = open ('wormhole.out', 'w')

vals = fin.read().splitlines() #gets every line

total = int(vals[0])

pos = []

for i in range(1, total+1):
    t = list(map(int, (vals[i]).split(" ")))
    pos.append(t)

print(pos)


fout.write( "yes"+ "\n")