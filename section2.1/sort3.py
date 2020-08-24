"""
ID: ashayp21
LANG: PYTHON3
TASK: sort3
"""
fin = open ('sort3.in', 'r')
fout = open ('sort3.out', 'w')

vals = fin.read().splitlines() #gets every line
N = int(vals[0])

have = []
for i in range(N):
    have.append(int(vals[i+1]))

print(have)


# def sort_012(input_list):
#     """
#     The idea is to put 0 and 2 in their correct positions, which will make sure
#     all the 1s are automatically placed in their right positions
#     """
#     # initialize pointers for next positions of 0 and 2
#     next_pos_0 = 0
#     next_pos_2 = len(input_list) - 1
#
#     front_index = 0
#     A = 0
#     while front_index <= next_pos_2:
#         if input_list[front_index] == 1:
#
#             if input_list[next_pos_0] != input_list[front_index]:
#                 input_list[front_index] = input_list[next_pos_0]
#                 input_list[next_pos_0] = 1
#                 print("swapped %i and %i" % (front_index, next_pos_0))
#                 A += 1
#             next_pos_0 += 1
#             front_index += 1
#         elif input_list[front_index] == 3:
#             if input_list[next_pos_2] != input_list[front_index]:
#                 input_list[front_index] = input_list[next_pos_2]
#                 input_list[next_pos_2] = 3
#                 print("swapped %i and %i" % (front_index, next_pos_2))
#                 A += 1
#             next_pos_2 -= 1
#         else:
#             front_index += 1
#     return A

# ans = sort_012(arr)
# print(arr)

ans = 0

want = sorted(have)

n = 0
for i in range(N):
    for j in range(N):
        if  have[i] != want[i] and have[j] != want[j] and have[i] == want[j] and have[j] == want[i]:
            n += 1
            have[i] = want[i]
            have[j] = want[j]

print(have)
print(n)
c = 0
for i in range(N):
    if have[i] != want[i]:
        c += 1

ans = (c // 3) * 2 + n
print(ans)

fout.write(str(ans) + "\n")


