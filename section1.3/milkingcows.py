"""
ID: ashayp21
LANG: PYTHON3
TASK: milk2
"""
fin = open ('milk2.in', 'r')
fout = open ('milk2.out', 'w')


#get data
vals = fin.read().splitlines() #gets every line

num_cows = int(vals[0])
times = vals[1:len(vals)]

start_stop = []

max = 0
min = 100000000000

for i in range(num_cows):
    temp = times[i].split(" ")
    start = int(temp[0])
    stop = int(temp[1])

    if stop > max:
        max = stop
    if start < min:
        min = start
    start_stop.append([start, stop])


milking = 0
idle = 0

current_m = 0
current_i = 0


def checkMilking(time):
    for i in range(len(start_stop)):
        if start_stop[i][0] <= time < start_stop[i][1]: #milking
            t = start_stop[i][1] - time #don't subtract startstop[i][0] because time might be greater than that
            start_stop.pop(i)
            return True, t
    return False, 0

is_milking = True

i = min

while i < max:
    is_milking, time = checkMilking(i)
    if is_milking:

        if current_i > idle:
            idle = current_i

        current_i = 0
        current_m += time
        i += time #skip ahead, don't have to increment by 1
    else:
        if current_m > milking:
            milking = current_m

        current_m = 0
        current_i += 1
        i += 1

if current_i > idle:
    idle = current_i

if current_m > milking:
    milking = current_m

fout.write (str(milking) + " " + str(idle) + "\n")
