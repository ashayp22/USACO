"""
ID: ashayp21
LANG: PYTHON3
TASK: ariprog
"""
fin = open ('ariprog.in', 'r')
fout = open ('ariprog.out', 'w')

vals = fin.read().splitlines() #gets every line

N = int(vals[0]) #length of progressions
M = int(vals[1]) #upper bound

total = 0

bisquares = []

for i in range(0, M+1):
    for j in range(0, M+1):
        bisquares.append(i**2 + j**2)

bisquares = list(dict.fromkeys(bisquares))
max_b = (M * M) * 2

quick_lookup = [0] * (max_b + 1)

# for i in range(0, max_b):
#     quick_lookup[str(i)] = False

for b in bisquares:
    quick_lookup[b] = 1

print("got list")

total = []
#
# for dif in range(1, int((max_bi-1)/(N-1))+1):
#     # print(dif)
#     for square in bisquares:
#         current = square
#         found = True
#         for j in range(1, N):
#             current += dif
#             if current > max_bi or not quick_lookup[str(current)]:
#                 found = False
#                 break
#         if found:
#             total.append([square, dif])


# for square in bisquares:
#     print(square)
#     current = square
#     for dif in range(1, (max_bi-square) // (N-1)):
#         found = True
#         for j in range(1, N):
#             current += dif
#             if current > max_bi or not quick_lookup[str(current)]:
#                 found = False
#                 break
#         if found:
#             total.append([square, dif])


for i in range(0, M * M * 2):
    # print(i)
    if not quick_lookup[i]:
        continue

    for dif in range(1, (max_b-i) // (N-1) + 1):
        found = True
        for j in range(1, N):
            if not quick_lookup[i + dif * j]:
                found = False
                break
        if found:
            total.append([i, dif])

new_list = []

print("sorting")

for a in total:
    num = a[0]
    dif = a[1]
    if len(new_list) == 0:
        new_list.append(a)
        continue
    i = 0

    while (i < len(new_list)) and (new_list[i][1] < dif):
        i += 1

    while (i < len(new_list)) and new_list[i][1] == dif and (new_list[i][0] < num):
        i += 1

    new_list.insert(i, a)


print(new_list)

'''
start with dif of 1, 2, 3, 4, ... max(bisquares)/2
check every num in the list

'''

ans = ""

if len(new_list) == 0:
    ans = "NONE\n"
else:
    for a in new_list:
        ans += str(a[0]) + " " + str(a[1]) + "\n"

fout.write (str(ans))
