"""[summary]
function to check if  the cow can be placed distance, x 
    may be returning the empty stalls might help?
    or we need to send back a boolean
    
    if all_placed
        them we can try increasing the space
    else
        we reduce the space


    
"""

def place_cow(stalls, cows , distance):
    """[summary]
    lets start returning the true or false 
    why do we need the input to be sorted? 
        because if it is not sorted, we will not be looking at the nearest cow position
        but we will be looking at last one which might be further then the one before that
        so it is critical that we sort the barn position
    Args:
        stalls - list
        cows - int
        distance - int
    """
    last_place_at = None
    for stall in stalls:
        if cows <= 0:
            break 
        if not last_place_at:
            last_place_at = stall 
            cows = cows - 1
        else:
            if abs(stall - last_place_at) >= distance :
                cows = cows - 1
                last_place_at = stall
    return False if cows > 0 else True

#print(place_cow(sorted([1,2,8,4,9]), 3, 3))

"""[summary]
we can actually place the cows at 1, 2,3,4,6... and so on to C 
for every C we will be doing full N scans
so the algorithm would be C * N 
we can reduce that complexity by using binary search to reduce the linear search space
    """

def max_distance(stalls , cow, low, high):
    if low >= high:
        return low
    else:
        mid = (low + high) // 2
        if place_cow(stalls, cow, mid):
            return max_distance(stalls, cow, mid, high)
        else:
            return max_distance(stalls, cow, low, mid-1) # as we could not place at mid
s = sorted([1, 2, 8, 4, 9])
print(max_distance(s, 3, 0, 5 ))

