"""
ID: ashayp21
LANG: PYTHON3
TASK: namenum
"""
fin = open ('namenum.in', 'r')
fout = open ('namenum.out', 'w')

name = open ('dict.txt', 'r')

#get data
vals = fin.read().splitlines() #gets every line

number = vals[0]

all_names = name.read().splitlines()

mapping = [["a", "b", "c"], ["d", "e", "f"], ["g", "h", "i"], ["j", "k", "l"],
["m", "n", "o"], ["p", "r", "s"], ["t", "u", "v"], ["w", "x", "y"]]

working_names = []


for name in all_names:
    if len(name) == len(number): #make sure that the length matches
        matches = True
        for i in range(len(name)):
            letter = name[i:i+1] #the letter
            num = int(number[i:i+1])
            if not letter.lower() in mapping[num - 2]:
                matches = False
                break

        if matches:
            working_names.append(name)

txt = ""

for n in working_names:
    txt += n + "\n"

if txt == "":
    txt = "NONE\n"

fout.write (txt)
