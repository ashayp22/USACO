"""
ID: ashayp21
LANG: PYTHON3
TASK: milk3
"""
fin = open ('milk3.in', 'r')
fout = open ('milk3.out', 'w')

vals = fin.read().splitlines() #gets every line

line_1 = vals[0].split(" ")
A = int(line_1[0])
B = int(line_1[1])
C = int(line_1[2])

#solve

visited_states = dict() #all of the states that have been already visited
a_list = set()

def get_new(first, second, first_current, second_current):
    if first_current < second - second_current:
        return 0, second_current + first_current
    else:
        return first_current - (second - second_current), second

def milk(a, b, c, a_i, b_i, c_i):
    global visited_states, a_list
    current_state = (a_i, b_i, c_i)
    # print(current_state)
    if current_state in visited_states:
        # print("returned")
        return
    else:
        visited_states[current_state] = True

    if a_i == 0:
        a_list.add(c_i)

    #pour from a to b
    first_i, second_i = get_new(a, b, a_i, b_i)
    milk(a, b, c, first_i, second_i, c_i)

    #pour from a to c

    first_i, second_i = get_new(a, c, a_i, c_i)
    milk(a, b, c, first_i, b_i, second_i)

    #pour from b to a

    first_i, second_i = get_new(b, a, b_i, a_i)
    milk(a, b, c, second_i, first_i, c_i)

    #pour from b to c

    first_i, second_i = get_new(b, c, b_i, c_i)
    milk(a, b, c, a_i, first_i, second_i)

    #pour from c to a

    first_i, second_i = get_new(c, a, c_i, a_i)
    milk(a, b, c, second_i, b_i, first_i)

    #pour from c to b

    first_i, second_i = get_new(c, b, c_i, b_i)
    milk(a, b, c, a_i, second_i, first_i)

milk(A, B, C, 0, 0, C)

#ans

a_list = list(a_list)
a_list = sorted(a_list)

line = ""

for f in a_list:
    line += str(f) + " "

fout.write (line[0:len(line)-1] + "\n")