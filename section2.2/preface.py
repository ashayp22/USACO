"""
ID: ashayp21
LANG: PYTHON3
TASK: preface
"""
fin = open ('preface.in', 'r')
fout = open ('preface.out', 'w')

vals = fin.read().splitlines() #gets every line

max_num = int(vals[0])


def int_to_Roman(num):
    val = [
        1000, 900, 500, 400,
        100, 90, 50, 40,
        10, 9, 5, 4,
        1
    ]
    syb = [
        "M", "CM", "D", "CD",
        "C", "XC", "L", "XL",
        "X", "IX", "V", "IV",
        "I"
    ]
    roman_num = ''
    i = 0
    while num > 0:
        for _ in range(num // val[i]):
            roman_num += syb[i]
            num -= val[i]
        i += 1
    return roman_num

numerals = ["I", "V", "X", "L", "C", "D", "M"]
vals = [0, 0, 0, 0, 0, 0, 0]

dic = dict(zip(numerals, vals))

for i in range(1, max_num+1):
    roman_num = int_to_Roman(i)
    for a in roman_num:
        dic[a] += 1

ans = ""


for key in dic.keys():
    if dic[key] > 0:
        ans += key + " " + str(dic[key]) + "\n"

fout.write (str(ans))