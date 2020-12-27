def stack_sortable(A):
    stack = []
    output = []
    for x in A:
        while (len(stack) > 0 and stack[-1] < x):
            output.append(stack.pop())
        stack.append(x)
    while stack:
        output.append(stack.pop())
    return output


print(stack_sortable([3,1,2]))


"""
next smaller number
binary search tree pre order traversal is valid or no
"""