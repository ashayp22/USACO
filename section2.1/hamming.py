"""
ID: ashayp21
LANG: PYTHON3
TASK: hamming
"""
fin = open ('hamming.in', 'r')
fout = open ('hamming.out', 'w')

vals = fin.read().splitlines() #gets every line

first_line = vals[0].split(" ")
N = int(first_line[0])
B = int(first_line[1])
D = int(first_line[2])

def gen_codewords(current, max):
    if len(current) == max:
        return [current]
    all = []
    all += gen_codewords(current + "0", max)
    all += gen_codewords(current + "1", max)
    return all

#generate codewords
all = gen_codewords("", B)

#helper method: hamming distance
def hamming(a, b):
    c = 0
    for i in range(len(a)):
        if a[i] != b[i]:
            c += 1
    return c


big_arr = []
for a in all:
    big_arr.append([a, [a]])

#iterate through all of the codewords
for i in range(len(big_arr)):
    #compare to the other codewords
    for j in range(i, len(big_arr)):
        good = True
        for z in range(len(big_arr[i][1])):
            if hamming(big_arr[i][1][z], all[j]) < D:
                good = False
                break
        if good:
            big_arr[i][1].append(all[j])

#now, we find the answer

ans = []
#first, find the set of N codewords
for i in range(len(big_arr)):
    print(big_arr[i][1])
    if len(big_arr[i][1]) >= N:
        ans = big_arr[i][1].copy()[0:N]
        break

#now, we convert to decimal
print(ans)

def bit_to_num(a):
    t = 0
    for z in range(len(a)):
        t += 2**(len(a)-z-1) * int(a[z])
    return t

g = ""
c = 0
t = 0
for a in ans:
    if c == 10:
        g += "\n"
        c = 0
        g += str(bit_to_num(a)) + " "
    elif c == 9 or t == len(ans)-1:
        g += str(bit_to_num(a))
    else:
        g += str(bit_to_num(a)) + " "
    c += 1
    t += 1

print(t)

print(g)

fout.write(g + "\n")


