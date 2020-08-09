"""
ID: ashayp21
LANG: PYTHON3
TASK: skidesign
"""
fin = open ('skidesign.in', 'r')
fout = open ('skidesign.out', 'w')

vals = fin.read().splitlines() #gets every line

total = int(vals[0])

all_heights = []

for i in range(1, len(vals)):
    all_heights.append(int(vals[i]))

all_heights = sorted(all_heights)

min = all_heights[0]
max = all_heights[total - 1]

min_cost = None

for temp_min in range(min, max):

    temp_max = temp_min + 17
    temp_cost = 0
    for i in range(len(all_heights)):
        if all_heights[i] < temp_min:
            temp_cost += (temp_min - all_heights[i]) ** 2
        elif all_heights[i] > temp_max:
            temp_cost += (all_heights[i] - temp_max) ** 2

    if min_cost is None:
        min_cost = temp_cost
    elif min_cost > temp_cost:
        min_cost = temp_cost


# #set each element as a min
# #set each element after as a max until difference > 17
# #find cost for converting the ones before
#
# min_cost = 1000000000
# m1 = 0
# m2 = 0
#
# for i in range(len(all_heights)-1):
#     new_cost = 0
#     min_height = all_heights[i]
#     for z in range(0, i):
#         new_cost += (min_height - all_heights[z])**2
#     max_i = i
#     while max_i < len(all_heights) and (all_heights[max_i] - min_height) <= 17:
#         max_i += 1
#
#     #first, we try by not modifying the max
#     c1 = new_cost
#     c2 = new_cost
#     max_i -= 1
#     max_height = all_heights[max_i]
#     for z in range(max_i + 1, len(all_heights)):
#         c1 += (all_heights[z] - max_height)**2
#     #now, we try by modifying the max
#     if max_i != len(all_heights) - 1:
#         max_i += 1
#     max_height = all_heights[max_i]
#     c2 += (max_height - (min_height + 17))**2 #we have to decrease the max height
#     for z in range(max_i + 1, len(all_heights)):
#         c2 += (all_heights[z] - (min_height + 17))**2
#
#     min_c = min(c1, c2)
#     print(min_c)
#     if min_c < min_cost:
#         m1 = min_height
#         m2 = max_height
#         min_cost = min_c
#
# for i in range(len(all_heights)-1, 0, -1):
#     new_cost = 0
#     max_height = all_heights[i]
#     #first, we find the max cost
#     for z in range(i + 1, len(all_heights)):
#         new_cost += (all_heights[z] - max_height)**2
#     #now, we find the min
#     min_i = i
#     while min_i >= 0 and (max_height - all_heights[min_i]) <= 17:
#         min_i -= 1
#
#     #first, we try by not modifying the min
#     c1 = new_cost
#     c2 = new_cost
#     min_i += 1
#     min_height = all_heights[min_i]
#     for z in range(0, min_i):
#         c1 += (min_height - all_heights[z])**2
#
#     #now we modify the min
#
#     if min_i != 0:
#         min_i -= 1
#
#     min_height = all_heights[min_i]
#     c2 += ((max_height - 17) - min_height) ** 2  # we have to decrease the max height
#     for z in range(0, min_i):
#         c2 += ((max_height - 17) - all_heights[z]) ** 2
#
#     min_c = min(c1, c2)
#     print(min_c)
#     if min_c < min_cost:
#         m1 = min_height
#         m2 = max_height
#         min_cost = min_c
#
# print(m1)
# print(m2)

fout.write( str(min_cost) + "\n")