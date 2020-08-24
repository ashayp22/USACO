"""
ID: ashayp21
LANG: PYTHON3
TASK: holstein
"""
fin = open ('holstein.in', 'r')
fout = open ('holstein.out', 'w')

vals = fin.read().splitlines() #gets every line
num_vitamins = int(vals[0])
min_vitamins = [int(x) for x in vals[1].split(" ")]
num_feed = int(vals[2])
feeds_vitamins = [] #first dimension is every feed, second dimension is every vitamin

for i in range(3, 3 + num_feed):
    feeds_vitamins.append([int(x) for x in vals[i].split(" ")])

print(num_vitamins)
print(min_vitamins)
print(num_feed)
print(feeds_vitamins)

#iterate through all combinations
#minimize for the one that has the min number of scoops and min feedtype value

feed_types = [x for x in range(num_feed)]


def generate(current, types):
    if len(types) == 0:
        return [current]

    all = []
    types_copy = types.copy()
    a = types_copy.pop()
    all += generate(current, types_copy)
    current_copy = current.copy()
    current_copy.append(a)
    all += generate(current_copy, types_copy)

    return all

def sum(l):
    s = 0
    for a in l:
        s += a
    return s

all = generate([], feed_types)

minimum_scoops = None
sorted_list = []



for set in all:
    good_set = True
    for v in range(num_vitamins):
        min_v = min_vitamins[v]
        feed_val = 0
        for f in set:
            feed_val += feeds_vitamins[f][v]
        if min_v > feed_val: #minimum scoops aquired
            good_set = False
            break
    if good_set:
        if minimum_scoops is None:
            minimum_scoops = len(set)
            sorted_list = set
        elif minimum_scoops > len(set):
            minimum_scoops = len(set)
            sorted_list = set
        elif minimum_scoops == len(set):
            if sum(sorted_list) > sum(set):
                minimum_scoops = len(set)
                sorted_list = set

print(minimum_scoops)
print(sorted_list)

ans = ""

for f in sorted_list:
    ans = str(f+1) + " " + ans

ans = str(minimum_scoops) + " " + ans


fout.write(str(ans[0:-1]) + "\n")


