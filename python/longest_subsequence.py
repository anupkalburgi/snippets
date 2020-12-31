
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

def substring(S):
    if not S:
        return [[]]
    else:
        (x, xs) = S[0], S[1:]
        ssub = substring(xs)
        return ssub + [[x] + xss for xss in ssub] 

# print(substring("a"))
# print(substring("ab"))
# print(substring("abc"))

def lcs_brute_force(s1:str, s2: str) -> int:
    sub1 = substring(s1)
    sub2 = substring(s2)
    count = 0
    for ss1 in sub1:
        for ss2 in sub2:
            if "".join(ss1) == "".join(ss2):  
                print(ss1, ss2)
                count = max(count, len(ss1))
    return count
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
# TODO: generting substring vs generating subsequence
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