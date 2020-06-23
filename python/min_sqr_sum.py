def min_sqr_sum(num, count = 0):
    if num == 0:
        return count
    if num == 1:
        return count + 1 
    else:
        sq = 0
        res = 0
        for i in range(1, num + 1):
            sq = i * i
            if  sq <= num:
                res = sq 
            else:
                break
        return min_sqr_sum(num - res, count + 1)

print(min_sqr_sum(4))