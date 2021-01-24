"""[summary]
Aggressive Cows - 
Taken from https://www.spoj.com/problems/AGGRCOW/ 
actually understoon the problem by looking at https://www.youtube.com/watch?v=SutyzUvegdo&ab_channel=AnuragCodes 

the thing that was unclear was did the number represent the stall next to each other or actul gaps inbetween
so the way to think about his problem is imagining a liner line, 1 to n and the respective stalls place at
respective numbers

Steps,
1. Sort the input array (actully this might not be necessary as are going to scan the full array ? no but then we will
will not know should we try something beyong that ? may be writing code will make that clear )

2. and we go on see what is the maximum space we can leave between the cows, 
    first take 1, the check if we can place all the cows 
    then 2 

3. now doing that 1,2,3, is very expensive because we might be having a lot of stalls and corresponding cow 
    we can reduce the reducde that by using bianry search to guide us , and that way we can go down to log time

"""

def can_place(stalls, cows, last_placed):
    """
    Do we want to do this recursive or iterative, 

    Args:
        stalls ([type]): [description]
        cows ([type]): [description]
        last_placed ([type]): [description]
    """
