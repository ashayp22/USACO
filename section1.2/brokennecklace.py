"""
ID: ashayp21
LANG: PYTHON3
TASK: beads
"""
fin = open ('beads.in', 'r')
fout = open ('beads.out', 'w')


#get data
vals = fin.read().splitlines() #gets every line

num_beads = int(vals[0])
beads = vals[1]


max = 0

def adjustIndex(i, max):
    if i < 0:
        return max - 1
    if i >= max:
        return 0
    return i


for i in range(num_beads):
    left = 1
    right = 1

    lindex = adjustIndex(i - 1, num_beads)
    rindex = adjustIndex(i, num_beads)

    #check left and right
    l_bead = beads[lindex: lindex + 1]
    r_bead = beads[rindex: rindex + 1]

    go_right = True
    go_left = True

    while go_right or go_left:

        #go left

        if go_left:

            lindex -= 1
            lindex =  adjustIndex(lindex, num_beads)

            if rindex == lindex:
                break

            l_bead2 = beads[lindex: lindex + 1]

            if l_bead == "w":
                l_bead = l_bead2
                left += 1
            elif l_bead2 == "w":
                left += 1
            elif l_bead == l_bead2:
                left += 1
            else:
                go_left = False

        #go right

        if go_right:

            rindex += 1

            rindex = adjustIndex(rindex, num_beads)

            if rindex == lindex:
                break

            r_bead2 = beads[rindex: rindex + 1]

            if r_bead == "w":
                r_bead = r_bead2
                right += 1
            elif r_bead2 == "w":
                right += 1
            elif r_bead == r_bead2:
                right += 1
            else:
                go_right = False


    if left + right > max:
        max = left + right


fout.write (str(max) + "\n")
