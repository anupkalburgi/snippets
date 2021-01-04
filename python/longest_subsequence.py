
"""
substring, 

"abc"
a
ab
abc 

b
bc 

c 


sunstring(ab) => [[], [a], [b],[a,b]]
"""

def substrings(lst):
    """
    n^2
    """
    subbs = []
    for i in range(len(lst)+1):
        for j in range(i, len(lst)+1):
            if len(lst[i:j]) > 0:
                subbs.append(lst[i:j]) 
    return subbs

def lcs_brute(s1, s2):
    subs1 = substrings(s1)
    subs2 = substrings(s2)
    max_len = 0 
    for ss1 in subs1:
        for ss2 in subs2:
            if ss1 == ss2:
                max_len = max(len(ss1), max_len)
    return max_len 

print(lcs_brute("abdca", "cbda"))
# print(lcs_brute_force("abdca", "cbda"))
"""
longest common substring
    
longest comomon subsequence
"""

def lcs(s1, s2, id1, id2, size):
    """
    complexity: 3^(m+n)
    """
    if id1 == len(s1) or id2 == len(s2):
        return size
    # c1 = size
    if s1[id1] == s2[id2]:
        return lcs(s1, s2, id1+1, id2+1, size+1)
    c2 = lcs(s1, s2, id1+1, id2, 0)
    c3 = lcs(s1 , s2, id1, id2+1, 0)
    
    return max(size, c2, c3)


def lcs_memo(s1, s2):
    """
    longest possible would be the len of the stortest string i.e the count
    we will have a tree dimensional thing
    """
    maxLen = min(len(s1), len(s2))
    memo = [[[-1 for _ in range(maxLen)] for _ in range(len(s2))] for _ in range(len(s1))]

    def lcs_string(s1, s2, i, j , size):
        if i == len(s1) or j == len(s2):
            return size
        if memo[i][j][size] == -1:
            c1 = size
            if s1[i] == s2[j]:
                c1 = lcs_string(s1, s2, i+1, j+1, size+1)
            c2 = lcs_string(s1, s2, i+1, j,0)
            c3 = lcs_string(s1, s2, i, j+1, 0)
            memo[i][j][size] = max(c1, max(c2, c3))
        return memo[i][j][size]
    return lcs_string(s1, s2, 0 , 0, 0)

def lcs_dp(s1, s2):
    """
    complexity is m * n
    """
    dp = [[0 for _ in range(len(s2)+1)] for _ in range(len(s1)+1)]
    maxLen = -1
    for i in range(1, len(s1)+1):
        for j in range(1, len(s2)+1):
            if s1[i-1] == s2[j-1]:
                dp[i][j] = 1 + dp[i-1][j-1]
                maxLen = max(maxLen, dp[i][j])
    return maxLen



print("abdca", "cbda" , "expect 2 ->", lcs("abdca", "cbda", 0 , 0 , 0)) # 2
print("passport", "ppsspt", "expect 3 ->" , lcs("passport", "ppsspt", 0 ,0 ,0)) # 3
print(lcs_memo("abdca", "cbda"))
print(lcs_dp("abdcfa", "cbda"))

print("Substring End ###################################################")

###################################################
# subsequence, without changing the order, 
#  deleteing elements from the either
###################################################

def longest_subsequence(s1, s2, i, j):
    if i == len(s1) or j == len(s2):
        return 0
    else:
        if s1[i] == s2[j]:
            return 1 + longest_subsequence(s1, s2, i+1, j+1)
        c1 = longest_subsequence(s1, s2, i+1, j )
        c2 = longest_subsequence(s1, s2, i, j+1)
        return max(c1, c2)


def longest_subsequence_memo(s1, s2):
    memo = [[-1 for _ in  range(len(s2))] for _ in range(len(s1))]

    def lsm_rec(s1, s2, i, j):
        if i == len(s1)  or j == len(s2):
            return 0
        else:
            if memo[i][j] == -1:
                if s1[i] == s2[j]:
                    memo[i][j] = 1 + lsm_rec(s1, s2, i+1, j+1)
                else:
                    c2 = lsm_rec(s1, s2, i+1, j)
                    c3 = lsm_rec(s1, s2, i, j+1)
                    memo[i][j] = max(c2, c3)
                return memo[i][j]
            return memo[i][j]
            
    return lsm_rec(s1, s2, 0, 0)

def longest_subsequence_dp(s1, s2):
    dp = [[0 for _ in range(len(s2)+1)] for _ in range(len(s1)+1)]
    max_len = 0
    for i in range(1, len(s1)+1):
        for j in range(1, len(s2)+1):
            if s1[i-1] == s2[j-1]:
                dp[i][j] = 1 + dp[i-1][j-1]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
            max_len = max(max_len, dp[i][j])
    return max_len


assert longest_subsequence("abdca", "cbda", 0 , 0) == 3
assert longest_subsequence("passport", "ppsspt", 0, 0) == 5
assert longest_subsequence_memo("abdca", "cbda") == 3
assert longest_subsequence_memo("passport", "ppsspt") == 5
print("abdca", "cbda" , "expect 3 -> lcs ->>", longest_subsequence("abdca", "cbda", 0 , 0)) 
print("passport", "ppsspt", "expect 5 -> lcs_memo ->>" , longest_subsequence_memo("passport", "ppsspt"))

print("abdca", "cbda" , "expect 3 -> lcs_dp ->>", longest_subsequence_dp("abdca", "cbda")) 
print("passport", "ppsspt", "expect 5 -> lcs_dp ->>" , longest_subsequence_dp("passport", "ppsspt"))

print("subsequence End ###################################################")
###################################################
# given 2 strings, s1, s2, what are the no. of inserts and deletes needed to transform s1 => s2
# n1 = len(s1)
# n2 = len(s2)
# lcs_len = lcs_dp(s1, s2)
# number_deletes = n1 - lcs_len 
# number_inserts = n2 - lcs_len
###################################################


def inserts_deletes_lcs(s1, s2):
    n1 = len(s1)
    n2 = len(s2)
    dp = [[0 for _ in range(n2+1)] for _ in range(n1+1)]
    lcs_len = 0
    
    for i in range(1, n1+1):
        for j in range(1, n2+1):
            if s1[i-1] == s2[j-1]:
                dp[i][j] = 1 + dp[i-1][j-1]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
            lcs_len = max(lcs_len, dp[i][j])
    
    return ((n1-lcs_len, n2-lcs_len))

print(inserts_deletes_lcs("abc", "fbc"))
print(inserts_deletes_lcs("abdca", "cbda"))
print(inserts_deletes_lcs("passport", "ppsspt"))


print("Longest increating subsequence ###################################################")
###################################################
# input 4,2,3,6, 10, 1, 12
# ouput 5 (2,3,6,10,12)
# 
# brute force generte all the subsequences,
# the filter out all the once that are not increasing order
# for i in range(1, len(s)):
#   if s[i-1] > s[i]:
#       reuturn False
#  return true
###################################################


def subsequence_lst(A):
    if len(A) == 0:
        return [[]]
    else:
        x, xs = A[0], A[1:]
        subbs = subsequence_lst(xs)
        return subbs + [[x]+ xss for xss in subbs]
    return subbs

def inc_list(s):
    for i in range(1, len(s)):
        if s[i-1] > s[i]:
            return False # a better way you have been to all()
    return True

def brute_lis(A):
    a_subs = subsequence_lst(A)
    inc_lists = []
    for ll in a_subs:
        if inc_list(ll):
            inc_lists.append(ll)
    return max(map(lambda x: len(x), inc_lists))
    
assert brute_lis([4, 2, 3, 6, 10, 1, 12]) == 5
assert brute_lis([-4, 10, 3, 7, 15]) == 4
print(brute_lis([4, 2, 3, 6, 10, 1, 12]))
print(brute_lis([-4, 10, 3, 7, 15]))


def lis(A, current, prev):
    """
    this solution is 2^n solution as there are 2 recursive call 

    """
    if len(A) == current:
        return 0
    else:
        c1 = 0
        if prev == -1 or A[prev] < A[current]:
            c1 = 1 + lis(A, current = current+1, prev=current)
        c2 = lis(A, current=current+1, prev=prev)
        return max(c1, c2)

assert lis([4, 2, 3, 6, 10, 1, 12], 0, -1) == 5
assert lis([-4, 10, 3, 7, 15], 0, -1) == 4
# print(lis([4, 2, 3, 6, 10, 1, 12], 0, -1))
# print(lis([-4, 10, 3, 7, 15], 0, -1))


def lis_memo(A):
    memo = [[-1 for _ in range(len(A)+1)] for _ in range(len(A)+1)]
    return lis_help(A, 0, -1, memo)
    
def lis_help(A, cur, prev, memo):
    """
    there are overlapping subproblems, which we cna
    and by caching, we will be doing n^2 solition
    """
    if cur == len(A):
        return 0
    else:
        if memo[cur][prev] == -1:
            c1 = 0 
            if prev == -1 or A[cur] > A[prev] :
                c1 = 1 + lis_help(A, cur+1, cur, memo)
            c2 = lis_help(A, cur+1, prev, memo)
            memo[cur][prev] = max(c1, c2)
            return memo[cur][prev]
        else:
            return memo[cur][prev]
    

assert lis_memo([4, 2, 3, 6, 10, 1, 12]) == 5
assert lis_memo([-4, 10, 3, 7, 15]) == 4
print(lis_memo([4, 2, 3, 6, 10, 1, 12]))
print(lis_memo([-4, 10, 3, 7, 15]))



def lis_dp(A):
    """
    the above solution is n^2
    and that will hit a stackoverflow for a big enough problem
    we do a n^2 algorithm using a single array 
    """
    dp = [1 for _ in range(len(A)+1)] # why is not initialized to 1
    max_len = 0 

    for i in range(1, len(A)):
        for j in range(i):
            if A[i] > A[j] and dp[i]  <= dp[j]:
                dp[i] =  dp[j] + 1
                max_len = max(dp[i], max_len)
    return max_len 

assert lis_dp([4, 2, 3, 6, 10, 1, 12]) == 5
assert lis_dp([-4, 10, 3, 7, 15]) == 4
print(lis_dp([4, 2, 3, 6, 10, 1, 12]))
print(lis_dp([-4, 10, 3, 7, 15]))
