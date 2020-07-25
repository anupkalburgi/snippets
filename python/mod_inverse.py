def find_additive_inverse_modn(num, mod):
    least = num / mod
    if least > 1:
        num = num % mod
    return mod - num

print(find_additive_inverse_modn(855, 97))
