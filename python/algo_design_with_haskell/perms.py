from typing import List
import itertools


'''
Answer taken from https://stackoverflow.com/a/17391851
I like it for the simplicity of it, and resembels like it is in haskell.
The for comprehension was the tirckey one, 
The recursive insert is more confusing than the iterative at the same compexity.
This was of generting the permutations are called inductive 
So this is a n^2 thing, 

[(x,y) for x in [1,2,3] for y in [3,4,5]]
[(1, 3), (1, 4), (1, 5), (2, 3), (2, 4), (2, 5), (3, 3), (3, 4), (3, 5)]

'''

def perms(inl: List[int]) -> List[List[int]]:
    if len(inl) == 0:
        return [[]]
    else:
        return [x for y in perms(inl[1:]) for x in inserts1(inl[0], y)]
            

def inserts(x: int, xs: List[int]) -> List[List[int]]:
    if len(xs) == 0:
        return [[x]]
    else:
        y = xs[:1]
        yss = xs[1:]
        return [[x] + y + yss] + list(map(lambda lss: y + lss , inserts(x, yss)))

def inserts1(x: int, xs: List[int]) -> List[List[int]]:
    return [xs[0:i]+ [x] + xs[i:] for i in range(len(xs)+ 1) ]


def picks(ins):
    if len(ins) == 0:
        return []
    else:
        x = ins[0]
        xs = ins[1:]
        return [(x, xs)] + [(y, [x] + ys) for (y, ys) in picks(xs)]

print(picks([1,2,3]))


'''
Here my under standing of what needs to be done was wrong
may is a linear pass, in reality i wanted a map inside a map
'''
# This looks correct but it is not as, calling insert on [[]] , 3 would yield [[[3]]]
# def perms(inl: List[int]) -> List[List[int]]:
#     if len(inl) == 0:
#         return [[]]
#     else:
#         x = inl[0]
#         xs = inl[1:]
#         ys = perms(xs)
#         tmp = list(map(lambda yss: inserts(x, yss), ys)) # [[]]
#         return tmp
            

# def inserts(x: int, xs: List[int]) -> List[List[int]]:
#     if len(xs) == 0:
#         return [[x]]
#     else:
#         y = xs[:1]
#         yss = xs[1:]
#         return [[x] + y + yss] + list(map(lambda lss: y + lss , inserts(x, yss)))


# print(inserts(1, []))
# print(list(perms([1,2,3])))



