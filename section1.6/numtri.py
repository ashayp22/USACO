"""ID: ashayp21LANG: PYTHON3TASK: numtri"""fin = open ('numtri.in', 'r')fout = open ('numtri.out', 'w')vals = fin.read().splitlines() #gets every linerows = int(vals[0])triangle = []for i in range(1, rows + 1):    r = vals[i].split(" ")    for z in range(len(r)):        r[z] = int(r[z])    triangle.append(r)max_sum = 0#solvedef get_max(a,b):    if a > b:        return a    return bl = [triangle[0][0]]for i in range(1, len(triangle)):    new_l = [0] * len(triangle[i])    # print(triangle[i])    for j in range(len(l)):        new_l[j] = get_max(new_l[j], l[j] + triangle[i][j])        new_l[j+1] = get_max(new_l[j+1], l[j] + triangle[i][j+1])    print(new_l)    l = new_lmax_sum = max(l)# print(triangle)fout.write (str(max_sum) + "\n")