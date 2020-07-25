def random_sequence(c, m, i, res, rn):
    '''
    n atleast c times 2
    '''
    if len(res) == (c * 2):
        return res
    else:
        rnn = (rn * m + i) % c
        return random_sequence(c, m, i, res + [rnn], rnn)

print(random_sequence(5, 2 , 1, [], 1))
print(random_sequence(5, 2 , 2, [], 1))
print(random_sequence(13, 2 , 0, [], 1))
