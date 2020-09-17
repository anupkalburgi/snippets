'''
in1 [2,3,3,5,5,6,7,7,8,12] 
in2 [5,5,6,8,8,9,10,10] 
o/p [5,6,8]

this can have both iterative and recursive solution

this is a good problem as it has
1. n^2 
2. nlogn
3. n 

All three solutions
'''

def intersection_sorted_arrays(arr1, arr2):
    # empty check
    i = 0
    j = 0
    res = []
    while i < len(arr1) and j < len(arr2):
        # there are there conditions
        # i == j
            # add to res
        # i < j
            # i++ also will have to do a while i is the same
        # i > j
            # j++ again will have to move till the elemment is the same 

        if arr1[i] == arr2[j]:
            if len(res) == 0  or res[-1] != arr1[i]:
                res.append(arr1[i])
            i = i + 1
            j = j + 1
            # while i > 0 and i < len(arr1):
            #     if arr1[i] == arr1[i-1]:
            #         i = i + 1
            #     else:
            #         break
            while j > 0 and j < len(arr2):
                if arr2[j] == arr2[j-1]:
                    j = j + 1
                else:
                    break
        elif arr1[i] < arr2[j]:
            i = i + 1
        elif arr1[i] > arr2[j]:
            j = j + 1
            

    return res

print(intersection_sorted_arrays([2,3,3,5,5,6,7,7,8,12] , [5,5,6,8,8,9,10,10]))
