"""
ID: ashayp21
LANG: PYTHON2
TASK: gift1
"""
fin = open ('gift1.in', 'r')
fout = open ('gift1.out', 'w')


#get data
vals = fin.read().splitlines() #gets every line

num_people = int(vals[0])

names = vals[1:num_people+1]

money = { i : 0 for i in names }

i = num_people + 1

while i < len(vals):
    #get person and their num
    line = vals[i+1].split(" ")
    n = vals[i] #name of person
    d = int(line[0]) #money of person
    p = int(line[1]) #num of people they will donate to
    o = vals[i+2:i+2+p] #the names of people they will donate to

    #first, person loses the money

    money[n] -= d

    for z in o:
        money[z] += int(d / p)

    if p != 0:
        money[n] += d % p #left overs

    i += 2 + p

#now we write
msg = ""

for n in names:
    msg += n + " " + str(money[n]) + "\n"

fout.write (msg)
