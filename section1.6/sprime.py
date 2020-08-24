"""
ID: ashayp21
LANG: PYTHON3
TASK: sprime
"""
fin = open ('sprime.in', 'r')
fout = open ('sprime.out', 'w')

vals = fin.read().splitlines() #gets every line

N = int(vals[0])

#helper

def isPrime(n):
    # Corner cases
    if (n <= 1):
        return False
    if (n <= 3):
        return True

    # This is checked so that we can skip
    # middle five numbers in below loop
    if (n % 2 == 0 or n % 3 == 0):
        return False

    i = 5
    while (i * i <= n):
        if (n % i == 0 or n % (i + 2) == 0):
            return False
        i = i + 6

    return True


#solution

start = [2, 3, 5, 7]

for i in range(1, N):
    pos = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    new_start = []

    for a in start:
        for p in pos:
            new_num = int(str(a) + str(p))
            if isPrime(new_num):
                new_start.append(new_num)
    start = new_start

#fout

ans = ""

for a in start:
    ans += str(a) + "\n"

fout.write (str(ans))