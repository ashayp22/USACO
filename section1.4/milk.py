"""
ID: ashayp21
LANG: PYTHON3
TASK: milk
"""
fin = open ('milk.in', 'r')
fout = open ('milk.out', 'w')

vals = fin.read().splitlines() #gets every line

first_line = vals[0].split(" ")
rest_lines = vals[1:len(vals)]
farmers = []

for r in rest_lines:
    current = list(map(int, r.split(" ")))
    # if len(farmers) == 0:
    #     farmers.append(current)
    # else:
    #     i = 0
    #     while i < len(farmers) and current[0] > farmers[i][0]:
    #         i += 1
    #     farmers.insert(i, current)
    farmers.append(current)


farmers = sorted(farmers, key=lambda x: x[0])

cost = 0
left = int(first_line[0])
num_farmers = int(first_line[1])

# print(left)
#
# print(farmers)

for f in range(num_farmers):
    farmer_cost = farmers[f][0]
    farmer_unit = farmers[f][1]

    if farmer_unit < left:
        left -= farmer_unit
        cost += farmer_unit * farmer_cost
    else:
        cost += left * farmer_cost
        left = 0
    # print(cost)
    if left == 0:
        break

fout.write (str(cost) + "\n")


