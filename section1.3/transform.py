"""
ID: ashayp21
LANG: PYTHON3
TASK: transform
"""
fin = open ('transform.in', 'r')
fout = open ('transform.out', 'w')


#get data
vals = fin.read().splitlines() #gets every line

n = int(vals[0])
before = vals[1:n+1]
after = vals[n+1:len(vals)]

#check 1 - 7

#rotates an array clockwise 90 degrees
def rotateArray(arr, l):
    newarr = []

    for i in range(l):
        str = ""
        for j in range(l):
            str += arr[l-j-1][i:i+1]
        newarr.append(str)
    return newarr

#reflect an array

def reflectArray(arr, l):
    newarr = []

    for i in range(l):
        str = ""
        for j in range(l):
            str += arr[i][l-j-1:l-j]
        newarr.append(str)
    return newarr


transformation = 7
found = False

def check1(arr):
    global transformation, found
    if rotateArray(arr, n) == after:
        transformation = 1
        found = True

def check2(arr):
    global transformation, found
    if not found:
        if rotateArray(rotateArray(arr, n), n) == after:
            transformation = 2
            found = True


def check3(arr):
    global transformation, found
    if not found:
        if rotateArray(rotateArray(rotateArray(arr, n), n), n) == after:
            transformation = 3
            found = True

def check4(arr):
    global transformation, found
    if not found:
        if reflectArray(arr, n) == after:
            transformation = 4
            found = True

def check5(arr):
    global transformation, found
    if not found:
        reflected = reflectArray(arr, n)
        if rotateArray(reflected, n) == after or rotateArray(rotateArray(reflected, n), n) == after \
                or rotateArray(rotateArray(rotateArray(reflected, n), n), n) == after:
            transformation = 5
            found = True



def check6(arr):
    global transformation, found
    if not found:
        if arr == after:
            transformation = 6
            found = True

checks = [check1, check2, check3, check4, check5, check6]

for i in range(6):
    checks[i](before)

fout.write (str(transformation) + "\n")
