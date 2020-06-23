'''
Given a list of meeting times, checks if any of them overlaps. 
The follow-up question is to return the minimum number of rooms required to accommodate all the meetings.
Given an array of time intervals (start, end) for classroom lectures (possibly overlapping), find the minimum number of rooms required.

For example, given [(30, 75), (0, 50), (60, 150)], you should return 2.


First Part of the QuestionL
- As there any overlapping meetings/classes/intervals?
Follow up
- How many rooms needed/no of intervals

examples
[(1, 4), (5, 6), (8, 9), (2, 6)] - True, 2
[(1, 4), (3, 6), (8, 9), (2, 6)] - True 3

$n^2$ is possible, for each interval go and check everyone of them if there is a overlap

input_len = len(input_intervals) + 1
rm_cnt = 0
for i in range(0, input_len):
    for j in range(i, input_len)):
        if over_lapping():
            rm_cnt = rm_cnt + 1
            
'''

def over_lapping(i1, i2):
    fs = i1[0]
    fe = i1[1]

    ss = i2[0]
    se = i2[1]
    print(i1, i2)
    print(ss < fe)
    return ss < fe

def over_lapping_intervals(input_intervals):
    input_len = len(input_intervals)
    rm_cnt = 0
    for i in range(0, input_len):
        for j in range(i + 1, input_len):
            if over_lapping(input_intervals[i], input_intervals[j]):
                rm_cnt = rm_cnt + 1

    return rm_cnt



'''
approach 2
Sort the input intervals by the starting 
then write a recursive function that can keep track of what is max endoing point
n log n solution
'''


def over_lapping_intervals_v2(intervals):
    sorted_intervals = sorted(intervals, key= lambda x: x[0])
    
    def do(ints, max_end, over_lap_count):
        if not ints:
            return over_lap_count
        else:
            head = ints[:1][0]
            tl = ints[1:]
            if max_end > head[0]:
                return do(tl, max(max_end, head[1]),  over_lap_count + 1)
            else:
                # No overlap,
                return do(tl, max(max_end, head[1]), over_lap_count)
    return do(sorted_intervals, 0, 0)


intervals = [(1, 4), (5, 6), (8, 9), (2, 6)]
insts =     [(30, 75), (0, 50), (60, 150)]
print(over_lapping_intervals_v2(intervals))
print(over_lapping_intervals_v2(insts))
