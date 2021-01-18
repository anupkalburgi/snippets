"""
Generate numbers from 1 to n, and arrange them in lexical Order 
1. generate all the numbers, cast that to the a string, and then sort it. that is O(nlogn$)
2. Now using DFS we can we can get this solution down to linear time 
"""
result = []
def dfs(curr, n):
    if curr > n:
        return
    result.append(curr)
    for i in range(0, 10):
        ne = curr * 10 + i
        if ne > n:
            return
        dfs(ne, n)


def lexical_order_dfs(n):
    for i in range(1, 10):
        result =  dfs(i, n)

lexical_order_dfs(31)
print(result)