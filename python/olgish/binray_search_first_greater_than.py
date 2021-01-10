def first_element_greater_than(sorted_arr, target):
    left , right = 0, len(sorted_arr) -1
    A =  sorted_arr
    while left < right:
        mid =  (right +  left) // 2  # left + ((right - left) // 2)
        if A[mid] >= target:
            right = mid
        else:
            left = mid +1 # as A[mid] < target
    return left

print(first_element_greater_than([1, 2, 4, 5], 3))
assert first_element_greater_than([1, 2, 4, 5], 3) == 2


def first_element_smaller_than(A, target):
    left , right = 0 , len(A) -1

    while left <right:
        mid = (left + right )  // 2

    if A[mid] >= target:
            right = mid
        else:
            left = mid + 1
    return left -1

print(first_element_smaller_than([1,2,4,5], 3))
assert first_element_smaller_than([1,2,4,5], 3) == 1