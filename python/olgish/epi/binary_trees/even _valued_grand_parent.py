
# sumEvenGrandparent(6,F,F)

# evengp(6, f,f)
#     evngp(7,t,f)
#         evengp(2,)

go(6,n,n)
    l = go(7,6,n) 
        l = go(2,7,6)
            l = go(9,2,7)
                l = do(none,9,2)    
                l = 0
                r = go(none,9,2)
                r = 0
                t,f -> f :
                else : t
                    l + r = 0 + 0 
                    0
            l = 0
            r = go (none,7,6)
                r = 0
                return 0 + 0 + 2 = 2
                

def print_event(elem):
    if elem % 2 == 0:
        return True

print((print_event(4)))
print(print_event(6))
print(print_event(7))