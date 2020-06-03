"""
ID: ashayp21
LANG: PYTHON3
TASK: palsquare
"""
fin = open ('palsquare.in', 'r')
fout = open ('palsquare.out', 'w')

#get data
vals = fin.read().splitlines() #gets every line

base = int(vals[0])

#parameters: num must be a string
def checkPalindrome(num):
    l = len(num)
    for i in range(int(l / 2)):
        if num[i:i+1] != num[l - i - 1: l - i]:
            return False
    return True


all_digits = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B",
              "C", "D", "E", "F", "G", "H", "I", "J"]

def convertBase(num, newBase):
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

good = []

for i in range(1, 301):
    square = i * i
    converted = convertBase(square, base)
    if checkPalindrome(converted):
        good.append([str(convertBase(i, base)), converted])

txt = ""

for g in good:
    txt += g[0] + " " + g[1] + "\n"

fout.write (txt)
