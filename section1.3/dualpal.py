"""
ID: ashayp21
LANG: PYTHON3
TASK: dualpal
"""
fin = open ('dualpal.in', 'r')
fout = open ('dualpal.out', 'w')

#get data
vals = fin.read().splitlines() #gets every line

vals = vals[0].split(" ")
N = int(vals[0])
S = int(vals[1])

#parameters: num must be a string
def checkPalindrome(num):
    l = len(num)
    for i in range(int(l / 2)):
        if num[i:i+1] != num[l - i - 1: l - i]:
            return False
    return True

def convertBase(num, newBase):
    all_digits = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B",
                  "C", "D", "E", "F", "G", "H", "I", "J"]

    largest_digit = 0
    while newBase**largest_digit <= num:
        largest_digit += 1

    largest_digit -= 1

    newNum = ""
    while largest_digit >= 0:
        digit = int(num / newBase**largest_digit)
        num -= digit * newBase**largest_digit
        newNum += all_digits[digit]
        largest_digit -= 1

    return newNum

nums = 0
starting = S + 1

all_numbers = []

while nums != N:
    is_pal = 0
    for base in range(2, 11):
        converted = convertBase(starting, base)

        if checkPalindrome(converted):
            is_pal += 1

        if is_pal >= 2:
            break

    if is_pal >= 2:
        nums += 1
        all_numbers.append(str(starting))

    starting += 1

txt = ""

for n in all_numbers:
    txt += n + "\n"

fout.write (txt)
