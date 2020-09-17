def subarray(inl):
    n = len(inl)
    for i in range(n+1):
        print(inl[:i])
        #TODO: do it right 

print(subarray([1,2,3]))

'''
1
1,2
1,2,3

2
2,3

3

'''