
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
    if s1[id1] == s2[id2]:
        size = lcs(s1, s2, id1+1, id2+1, size+1)
    c1 = lcs(s1, s2, id1+1, id2, 0)
    c2 = lcs(s1 , s2, id1, id2+1, 0)
    
    return max(size, max(c1, c2))


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



print(lcs("abdca", "cbda", 0 , 0 , 0))
print(lcs_memo("abdca", "cbda"))
print(lcs_dp("abdcfa", "cbda"))

