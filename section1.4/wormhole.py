"""
ID: ashayp21
LANG: PYTHON3
TASK: wormhole
"""
fin = open ('wormhole.in', 'r')
fout = open ('wormhole.out', 'w')

vals = fin.read().splitlines() #gets every line

total = int(vals[0])

pos = {}
keys = [] #each letter represents a wormhole

#each letter points to a position

for i in range(1, total+1):
    t = list(map(int, (vals[i]).split(" ")))
    pos[chr(64 + i)] = t
    keys.append(chr(64 + i))



#create wormholes
def createPairings(letters): #how many holes need to still be paired
    if len(letters) == 2: #base case, only two remain
        return [[letters[0], letters[1]]]

    all_pairs = [] #all of the pairs

    for i in range(1, len(letters)):
        l = letters.copy()
        new_pair = [l[0], l[i]] #automatically pair the first letter with the other letter
        #remove them from the list
        l.pop(0)
        l.pop(i-1)

        more_pairs = createPairings(l) #get the rest of the pairs

        for m in more_pairs: #for each of the returned pairs
            all_pairs.append(m + new_pair) #add the new pair to the end and then append

    return all_pairs


all_pairs = createPairings(keys)

num = 0

def findCircle(currentLetter, startLetter, pairs, positions):
    #in this method, we are looking for a circle or the end
    # print("we looking for "  + startLetter)
    # print("we at " + currentLetter)

    #base case: if we find a letter that is the start letter, return true
    # if currentLetter == startLetter:
    #     return True

    #first, we move in the +x direction

    closest_x = None
    chosen_i = -1

    current_x = positions[currentLetter][0]
    current_y = positions[currentLetter][1]


    for l in range(len(pairs)):
        letter = pairs[l]
        new_x = positions[letter][0]
        new_y = positions[letter][1]
        if new_y == current_y: #on the same line
            if new_x > current_x: #farther in the x direction
                if closest_x is None: #no x is set
                    closest_x = new_x
                    chosen_i = l
                elif new_x < closest_x: #this letter is closer
                    closest_x = new_x
                    chosen_i = l

    if closest_x is None: #cow reached the end
        return False
    if pairs[chosen_i] == startLetter: #we are at the start letter
        return True

    #now, we gotta move into this circle's wormhole

    if chosen_i % 2 == 0:
        chosen_i += 1
    else:
        chosen_i -= 1

    return findCircle(pairs[chosen_i], startLetter, pairs, positions)


    #check to see if there exists a letter that has a closest x pos to this letter
    #if we find a letter that is the start letter, return true
    #otherwise, we call findCircle again

    #if such a letter doesn't exist, then return false for no circle

z = 0
for pairs in all_pairs: #iterating through every possibility
    #iterate through each letter in pass
    # print(z)
    for i in range(len(pairs)):
        pairI = i - 1
        if i % 2 == 0:
            pairI = i + 1
        # print("new letter")
        if findCircle(pairs[pairI], pairs[i], pairs, pos): #found a circle
            # print("found for")
            # print(pairs[i])
            # print(pairs)
            num += 1
            break
    z += 1


fout.write( str(num) + "\n")