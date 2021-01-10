class Num:
    def __init__(self, val, index):
        self.num = val
        self.idx = index
        self.count = 0
    def __repr__(self):
        return   f'Num(num={self.num} idx={self.idx}, count={self.count})'
        


def merge(left, right):
    if  len(left)==0:
        return right
    if len(right) == 0:
        return left
    else:
        (lh, lt) = left[0], left[1:]
        (rh, rt) = right[0], right[1:]
 
        if lh.num < rh.num:
            return [lh] + merge(lt, right) 
        else:
            for l in left:
                l.count = l.count + 1
            return [right[0]] + merge(left, rt) # this where recursive might have a issue but this is when inc the count

def merge_sort(A):
    if len(A) <= 1:
        return A
    else:
        mid = len(A) // 2  
        left = merge_sort(A[:mid])
        right = merge_sort(A[mid:])
        return merge(left, right)
nums = []    
for idx , num in list(enumerate([5, 2, 6, 1])):
    nums.append(Num(num, idx))
sorted_nums = merge_sort(nums)

print("--------")
srt = sorted(sorted_nums, key= lambda x : x.idx, )
assert [x.count for x in srt]  == [2, 1, 1, 0]
print([ x.count for x in srt])
print([ x.idx for x in srt])
print([ x.num for x in srt])
# print(merge_sort([5, 2, 6, 1]))
# assert merge_sort([5, 2, 6, 1]) == [1, 2, 5, 6]
    