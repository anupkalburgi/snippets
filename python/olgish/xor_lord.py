def find_missing(A, n):
    """A is the input array, and n is the number till then 
    the idea is we go from 1 to n and xor with result
    and then go through A and xor, 
    all the duplicates will be eliminated expect for the one that has appread for 3 time
    """
    result = 0
    for i in range(1, n + 1):
        result = result ^ i
    for a in A:
        result = result ^ a
    return result

# aa = [i for i in range(1, 101)]
# print(find_missing(aa, 100))

# aa8 = aa[:7] + aa[8:]
# print(aa8)

# print(find_missing(aa8, 100))


def find_duplicate(A, n):
    """
    Idea is to go from 1, to n and xor the result
    then go trough the 1 to n, and xor the result
    the one that is duplicate will appear trice and will be in the result
    """

    result = 0

    for i in range(1, n+1):
        result = result ^ i

    for a in A:
        result = result ^ a 
    return result

a = [i for i in range(1,  101)]
a[9] = 2 
print(a)
print(find_duplicate(a, 100))