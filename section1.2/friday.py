"""
ID: ashayp21
LANG: PYTHON2
TASK: friday
"""

fin = open ('friday.in', 'r')
fout = open ('friday.out', 'w')

year = fin.read().splitlines() #gets every line

year = int(year[0]) + 1900
day = 2 # friday is last

num = [0, 0, 0, 0, 0, 0, 0]

for y in range(1900, year):
    days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    #check leap year
    if y % 100 == 0:
        if y % 400 == 0:
            days[1] += 1
    elif y % 4 == 0:
        days[1] += 1

    #start going
    for month in days:
        day += 12 #on the 13 now
        num[day % 7] += 1
        day += month - 12

#now we write
msg = ""

for n in num:
    msg += str(n) + " "

fout.write (msg[0:len(msg)-1] + "\n")
