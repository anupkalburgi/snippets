'''
given a array of numbers, return back the larged range in there
eg: 
input = [9,6,1,3,8,10,12,11] 
output = [8, 12]

Approach 1: 
Create a an array 
min,max = [9,6,1,3,8,10,12,11] = (1,12)
[0,0,0,0,0,0,0,0,0,0,0,0,0]
1 -> 0
2 -> 0
3 -> 0
4 -> 0
5 -> 0
6 -> 0
7 -> 0
8 -> 0
9 -> 0
10 -> 0
11 -> 0
12 -> 0

Would have to use ordred dict, but i dont see a advantage of using dict at all
1 -> 1
2 -> 0
3 -> 1
4 -> 0
5 -> 0
6 -> 0
7 -> 0
8 -> 1
9 -> 1
10 -> 1
11 -> 1
12 -> 1



max_len = 0
rangeB = None
rangeE = None
ans {
    max_len : [rangeB, rangeE]
}
for k, v in elm.iteritems():
    if v == 1:
        max_len = max_len + 1
        if rangeB == None: // range has not started
            rangeB = k
        elif rangeE != "a" : // range has begin, but can end here 
            rangeE = k
    else:
        # clear both bits and max_len
        ans.merge({max_len : (rangeA, rangeB)})
        max_len = 0
        rangeB = "a"
        rangeE = "a"

if rangeE != None and rangeB !=  None:
    ans.merge({max_len: (rangeB, rangeA))

Complexity of of this approach is leaner time 

Approach 2:
we sort it it, and write a linear recursive solution to identify the continues numbers
Complexity will be nLog(n) for sorting and n for identifying continues numbers 

'''