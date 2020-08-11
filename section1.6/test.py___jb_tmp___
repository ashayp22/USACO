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

all_palindrome_numbers = palindrome_number_generator()

for i in range(20):
    print(all_palindrome_numbers.__next__())

f = "101"
print("---")
print(f + f[-2::-1]) #tak
print(f + f[::-1])