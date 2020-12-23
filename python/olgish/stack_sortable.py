def stack_sortable(A):
    stack = []
    output = []
    for x in A:
        while (stack and stack[0] < x):
            output.append(stack.pop(0))
        stack.append(x)
    while stack:
        output.append(stack.pop(0))
    return output


print(stack_sortable([2,1,3]))