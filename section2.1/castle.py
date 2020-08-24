"""
ID: ashayp21
LANG: PYTHON3
TASK: castle
"""
fin = open ('castle.in', 'r')
fout = open ('castle.out', 'w')

vals = fin.read().splitlines() #gets every line

first_line = vals[0].split(" ")
M = int(first_line[0])
N = int(first_line[1])

plan = []
#creates the plan
for i in range(N):
    row_string = vals[1+i].split(" ")
    temp = []
    for j in range(M):
        module = int(row_string[j])
        print(module)
        c = 3
        walls = [False, False, False, False] #west, north, east, south
        while module != 0:
            if module - 2**c >= 0:
                module -= 2**c
                walls[c] = True
            c -= 1
        print(walls)
        temp.append(walls)
    plan.append(temp)

#finds an array with the size of each individual room

def checkBounds(n, m, N, M):
    return 0 <= n < N and 0 <= m < M

def expandRoom(plan, visited, c_i, c_j, N, M, size):
    # print("at %s %s" % (c_i+1, c_j+1))
    # print(plan[c_i][c_j])
    # print(visited)
    visited[c_i][c_j] = True
    # print(visited)

    size += 1
    #base case: can't move in any direction
    #check all four directions

    #south

    members = [[c_i, c_j]]

    if not plan[c_i][c_j][3]:
        new_c_i = c_i + 1
        new_c_j = c_j
        if checkBounds(new_c_i, new_c_j, N, M):
            # print(visited)
            if not plan[new_c_i][new_c_j][1] and not visited[new_c_i][new_c_j]: #north
                # print("moved down")
                size, visited, extraMembers = expandRoom(plan, visited, new_c_i, new_c_j, N, M, size)
                members += extraMembers

    #east
    if not plan[c_i][c_j][2]:
        new_c_i = c_i
        new_c_j = c_j + 1
        if checkBounds(new_c_i, new_c_j, N, M):
            if not plan[new_c_i][new_c_j][0] and not visited[new_c_i][new_c_j]: #west
                # print("moved right")
                size, visited, extraMembers = expandRoom(plan, visited, new_c_i, new_c_j, N, M, size)
                members += extraMembers

    #north

    if not plan[c_i][c_j][1]:
        new_c_i = c_i - 1
        new_c_j = c_j
        if checkBounds(new_c_i, new_c_j, N, M):
            if not plan[new_c_i][new_c_j][3] and not visited[new_c_i][new_c_j]: #south
                # print("moved up")
                size, visited, extraMembers = expandRoom(plan, visited,new_c_i,new_c_j, N, M, size)
                members += extraMembers

    #west
    if not plan[c_i][c_j][0]:
        new_c_i = c_i
        new_c_j = c_j - 1
        if checkBounds(new_c_i, new_c_j, N, M):
            if not plan[new_c_i][new_c_j][2] and not visited[new_c_i][new_c_j]: #east
                # print("moved left")
                size, visited, extraMembers = expandRoom(plan, visited,new_c_i,new_c_j, N, M, size)
                members += extraMembers

    # print("returning")
    return size, visited, members


def findRooms(plan, N, M):

    visited = []

    for x in range(N):
        t = []
        for y in range(M):
            t.append(False)
        visited.append(t)

    rooms = []
    size_rooms = []

    for _ in range(N):
        l = []
        for _ in range(M):
            l.append(0)
        size_rooms.append(l)

    k = 0
    # print(visited)
    for n in range(N):
        for m in range(M):
            if visited[n][m]:
                # print("visited %s %s" % (n,m))
                continue
            size, visited, members = expandRoom(plan, visited, n, m, N, M, 0)
            print(size)
            rooms.append(size)
            for a in members:
                size_rooms[a[0]][a[1]] = [size, k]
            k += 1
            # print("---------------next---------------")

    return rooms, size_rooms

print("--------------------------------------")
rooms, size_rooms = findRooms(plan, N, M)
print(size_rooms)
print(rooms)
num_rooms = len(rooms)
largest_room = max(rooms)

#now we find the optimal room to remove


def copyPlan(plan):
    new_plan = []
    for i in range(len(plan)):
        t = []
        for j in range(len(plan[i])):
            f = []
            for z in range(len(plan[i][j])):
                f.append(plan[i][j][z])
            t.append(f)
        new_plan.append(t)
    return new_plan

max_size = 0
side = ""
best_i = 0
best_j = 0

print("finding max")

for i in range(N):
    for j in range(M):
        #now, we create new plans by removing one wall

        #note: west, north, east, south

        #remove top

        if i >= 1 and plan[i][j][1]:

            if size_rooms[i][j][1] == size_rooms[i-1][j][1]:
                continue

            new_m = size_rooms[i][j][0] + size_rooms[i-1][j][0]
            print(new_m)
            if new_m > max_size:
                max_size = new_m
                side = "N"
                best_i = i
                best_j = j
            elif new_m == max_size:
                # check farthest west
                if j < best_j:  # it is farther west
                    max_size = new_m
                    side = "N"
                    best_i = i
                    best_j = j
                elif j == best_j:  # same west
                    # check farther south
                    if i >= best_i:  # farther south
                        max_size = new_m
                        side = "N"
                        best_i = i
                        best_j = j


        #remove right

        if j < M-1 and plan[i][j][2]:

            if size_rooms[i][j][1] == size_rooms[i][j+1][1]:
                continue

            new_m = size_rooms[i][j][0] + size_rooms[i][j+1][0]
            print(new_m)
            if new_m > max_size:
                max_size = new_m
                side = "E"
                best_i = i
                best_j = j
            elif new_m == max_size:
                #check farthest west
                if j < best_j: #it is farther west
                    max_size = new_m
                    side = "E"
                    best_i = i
                    best_j = j
                elif j == best_j: #same west
                    #check farther south
                    if i > best_i: #farther south
                        max_size = new_m
                        side = "E"
                        best_i = i
                        best_j = j


line = str(best_i+1) + " " + str(best_j+1) + " " + side
print(line)

ans = str(num_rooms) + "\n" + str(largest_room) + "\n" + str(max_size) + "\n" + line + "\n"

fout.write (str(ans))