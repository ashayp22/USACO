"""
ID: ashayp21
LANG: PYTHON3
TASK: pprime
"""
fin = open ('pprime.in', 'r')
fout = open ('pprime.out', 'w')

vals = fin.read().splitlines() #gets every line

def is_palindrome(num):
    return str(num) == str(num)[::-1]

def SieveOfEratosthenes(min, max):
    crossed = [] #starts at 0, ends with max(inclusive)
    for i in range(max+1):
        crossed.append(False)
    crossed[0] = True
    crossed[1] = True

    #now starts crossing out
    current_num = 2 #starting number

    while current_num**2 <= max:
        if not crossed[current_num]: #not yet crossed, can be a multiple
            for j in range(current_num*2, max+1, current_num): #every multiple of current num up till the max
                crossed[j] = True #is crossed now
        current_num += 1 #increases the current number

    #now gets list of primes
    primes = []
    for i in range(min, len(crossed)):
        if not crossed[i] and is_palindrome(i) and i >= min:
            primes.append(i)
    return primes

first_line = vals[0].split(" ")
a = int(first_line[0])
b = int(first_line[1])



#check if they are prime

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


#generate the palindromes

def palindrome_range(start,stop,step=1):

    ret = []
    for a in range(start, stop  + 1):
        if is_palindrome(a) and isPrime(a):
            ret.append(a)
    return ret

def palindrome_number_generator():
    yield 0
    lower = 1
    '''
    How this works:
    goes from 1-10, 100-1000, 1000-10000, and so on
    take temp = 101 for example
    you can generate palindrome with
    101 + 01 (third char is the center, last 2 is the reverse of the first two)
    or
    101 + 101 (temp + reverse(temp)
    '''
    while True:
        higher = lower*10
        for i in range(lower, higher):
            s = str(i)
            yield int(s+s[-2::-1]) #a + reverse(a[0:len(a)-1])
        for i in range(lower, higher):
            s = str(i)
            yield int(s+s[::-1]) #a + reverse(a)
        lower = higher



def palindromes(lower, upper):
    all_palindrome_numbers = palindrome_number_generator()
    for p in all_palindrome_numbers:
        if p >= lower and isPrime(p):
            break
    palindrome_list = [p]
    for p in all_palindrome_numbers:
        # Because we use the same generator object,
        # p continues where the previous loop halted.
        if p > upper:
            break
        if isPrime(p):
            palindrome_list.append(p)
    return palindrome_list


l = palindromes(a, b)
# print(l)

# l = SieveOfEratosthenes(a, b)

ans = ""

for a in l:
    ans += str(a) + "\n"

fout.write (str(ans))