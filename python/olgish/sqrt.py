def sqrt(x):
    """
    using the property of recursion
    """
    if x < 2:
        return x
    else:
        return 2 * sqrt(x // 4)

print(sqrt(9))