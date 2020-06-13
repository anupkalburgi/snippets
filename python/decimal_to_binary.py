def decimal_to_binary(num, rems):
    if num == 0:
        return rems[::-1]
    else:
        rem = num % 2
        rems.append(rem)
        return decimal_to_binary(num // 2, rems)

assert decimal_to_binary(193, []) == [1,1,0,0,0,0,0,1]


def binary_to_decimal(binary, place_value, decimal_value):
    '''
assuming the binary is numbers are given in list like [1,1,0,0,0,0,0,1] 
return back 193
counting from right to left is more convinent, as the base value goes on increasing by 2 every time
    '''
    if binary  == []:
        return decimal_value
    else:
        last_bit = binary.pop()
        return binary_to_decimal(binary, place_value *2, decimal_value + place_value * last_bit)

assert binary_to_decimal([1,1,0,0,0,0,0,1], 1, 0) == 193


def convert_decimal_binary(decimal, binary):
    if decimal == 0:
        return binary
    else:
        bin_part  = int(decimal * 2)
        remaining = (decimal * 2) - bin_part
        return convert_decimal_binary(remaining, binary + [bin_part])

assert convert_decimal_binary(0.25, []) == [0, 1]
