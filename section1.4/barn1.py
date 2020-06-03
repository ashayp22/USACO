"""
ID: ashayp21
LANG: PYTHON3
TASK: barn1
"""
fin = open ('barn1.in', 'r')
fout = open ('barn1.out', 'w')

vals = fin.read().splitlines() #gets every line

first_line = vals[0].split(" ")
cow_stalls = list(map(int, vals[1:len(vals)]))
max_boards = int(first_line[0])
total_stalls = int(first_line[1])
total_cow_stalls = int(first_line[2])

total_stalls_blocked = 0

cow_stalls = sorted(cow_stalls)

board_length = 2

differences = [] #difference, start, end

for c in range(1, len(cow_stalls)):
    differences.append([cow_stalls[c] - cow_stalls[c-1], cow_stalls[c-1], cow_stalls[c]])

differences = sorted(differences, key=lambda x: x[0], reverse = True)

trimmed_difference = differences[0:max_boards-1]
print(trimmed_difference)

borders = []

for t in trimmed_difference:
    borders.append(t[1])
    borders.append(t[2])

borders.append(min(cow_stalls))
borders.append(max(cow_stalls))

borders = sorted(borders)

for z in range(int(len(borders)/2)):
    total_stalls_blocked += borders[2 * z + 1] - borders[2 * z] + 1


fout.write (str(total_stalls_blocked) + "\n")
