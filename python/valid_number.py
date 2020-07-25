
def valid_symbol(input):
    '''
    Check if the number has proper sign on the left
    assuming
        no signs in between i.e. 1-10 etc
    check if left most bit is a sign
        if sign check if next bit is not sign
    '''
    symbols = set(['+', '-'])
    if not input:
        return False
    elif len(input) == 1:
        return 1
    else:
        left = input[0]
        lh = input[1]
        if left in symbols:
            if lh in symbols:
                return False
            else:
                return True
        else:
            return True
def valid_number(input):
    return valid_symbol(input)


# print(valid_number("-1"))
# print(valid_number("++1"))


def isNumber(s):
    """
    :type s: str
    :rtype: bool
    """
    
    #define state transition tables
    states = [
        # no State (0)
        {},
        # State (1) - Init state
        {'blank': 1, 'sign': 2, 'digit': 3, '.': 4}, 
        # State (2) - Signed - after finding +, -
        {'digit': 3, '.': 4}, 
        # State (3) - Digit
        {'digit': 3, '.': 5, 'e': 6, 'blank': 9},
        # State (4) - Don-digit dot
        {'digit': 5},
        # State (5) - After Dot
        {'digit': 5, 'e':6, 'blank': 9},
        # State (6) - Found 'e'
        {'digit': 8, 'sign': 7},
        # State (7) - Sign After 'e'
        {'digit': 8},
        # State (8) - Digit after 'e'
        {'digit': 8, 'blank': 9},
        # State (9) - Terminal
        {'blank': 9}
    ]
    
    current_state = 1
    for c in s:
        c_type = None
        if c >= '0' and c <='9':
            c_type = 'digit'
        elif c == "-" or c == "+":
            c_type = 'sign'
        elif c == " ":
            c_type = 'blank'
        else:
            c_type = c

        # if we can not move on, we end it here
        if c_type not in states[current_state]:
            return False
        
        current_state = states[current_state][c_type]

    # State 3, 5, 8, 9 are accepted terminal states.
    return current_state in [3, 5, 8, 9]
print(isNumber("6e-1"))