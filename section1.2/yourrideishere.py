"""
ID: ashayp21
LANG: PYTHON2
TASK: ride
"""
fin = open ('ride.in', 'r')
fout = open ('ride.out', 'w')
vals = fin.readlines()

comet = vals[0].split("\n")
group = vals[1].split("\n")

comet_val = 1
group_val = 1

for letter in comet[0]:
    comet_val *= ord(letter.lower()) - 96

for letter in group[0]:
    group_val *= ord(letter.lower()) - 96

if comet_val % 47 == group_val % 47:
    fout.write ('GO\n')
    fout.close()
else:
    fout.write ('STAY\n')
    fout.close()
