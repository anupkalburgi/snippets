def same_count(s1, s2, cnt):
    """
    return the count of elements that are same in both the string
    """
    if not s1 or not s2:
        return cnt
    else:
        (s1h, s1t) = s1[0], s1[1:]
        (s2h, s2t) = s2[0], s2[1:]
        if s1h != s2h:
            return cnt
        else:
            return same_count(s1t, s2t, cnt+1)


def only_typo(s1, s2):
    preffix = same_count(s1, s2, 0)
    suffix = same_count(s1[::-1], s2[::-1], 0)
    string_size = max(len(s1), len(s2))
    same_parts = preffix + suffix

    if string_size - same_parts <=1:
        return True
    else:
        return False

# s1 = 'yesterday'
# s2 = 'yesarday'
s1 = "adc"
s2 = "abc"
print(only_typo(s1, s2))