import string

class BTNode:
    def __init__(self, alpha):
        self.alphabet = alpha
        self.left = None
        self.right = None
        # I dont think I really need the left and right, but let me come back to it
    
    def __str__(self):
        return str(self.alphabet)

# def decode(input_str, m_tree, ans):
#     if input_str

def decode_morse_code_helper(input_code_char, morse_code_tree):
    if morse_code_tree is None:
        err = f"the tree is none cant proceed, invalid code"
        print(err)
        return err
    
    if input_code_char != "":
        x, xs = input_code_char[:1], input_code_char[1:]
        print(x, "$$$$$",xs)
        if x == ".":
            return decode_morse_code_helper(xs, morse_code_tree.left)
        if x == "-":
            return decode_morse_code_helper(xs, morse_code_tree.right)
        else:
            problem  = f"we are having a problem with {input_code_char}"
            print(problem)
            return problem
    else:
        return morse_code_tree.alphabet 
    



alphaBTNodesMap = {}
for a in string.ascii_letters:
    alphaBTNodesMap[a] = BTNode(a)

# print(alphaBTNodesMap)
emptyRoot = BTNode(None)
emptyRoot.left = alphaBTNodesMap['e']

alphaBTNodesMap['e'].left = alphaBTNodesMap['i']
alphaBTNodesMap['e'].right = alphaBTNodesMap['a'] 


alphaBTNodesMap['i'].left = alphaBTNodesMap['s']
alphaBTNodesMap['i'].right = alphaBTNodesMap['u']

alphaBTNodesMap['u'].left = alphaBTNodesMap['f']
alphaBTNodesMap['u'].right = None

alphaBTNodesMap['f'].left = None
alphaBTNodesMap['f'].right = None

alphaBTNodesMap['a'].left = alphaBTNodesMap['r'] 
alphaBTNodesMap['a'].right = alphaBTNodesMap['w']

alphaBTNodesMap['s'].left = alphaBTNodesMap['h'] 
alphaBTNodesMap['s'].right = alphaBTNodesMap['v']


alphaBTNodesMap['h'].left = None
alphaBTNodesMap['h'].right = None

alphaBTNodesMap['v'].left = None 
alphaBTNodesMap['v'] .right = None

alphaBTNodesMap['r'].left = alphaBTNodesMap['l'] 
alphaBTNodesMap['r'].right = None

alphaBTNodesMap['w'].left = alphaBTNodesMap['p']
alphaBTNodesMap['w'].right = alphaBTNodesMap['j']

emptyRoot.right = alphaBTNodesMap['t']

alphaBTNodesMap['t'].left = alphaBTNodesMap['n']
alphaBTNodesMap['t'].right = alphaBTNodesMap['m']


alphaBTNodesMap['n'].left = alphaBTNodesMap['d']
alphaBTNodesMap['n'].right = alphaBTNodesMap['k']

alphaBTNodesMap['d'].left = alphaBTNodesMap['b']
alphaBTNodesMap['d'].right = alphaBTNodesMap['x']

alphaBTNodesMap['b'].left = None
alphaBTNodesMap['b'].right = None

alphaBTNodesMap['x'].left = None
alphaBTNodesMap['x'].right = None

alphaBTNodesMap['k'].left = alphaBTNodesMap['c']
alphaBTNodesMap['k'].right =  alphaBTNodesMap['y']

alphaBTNodesMap['c'].left = None
alphaBTNodesMap['c'].right = None

alphaBTNodesMap['y'].left = None
alphaBTNodesMap['y'].right = None

alphaBTNodesMap['m'].left = alphaBTNodesMap['g']
alphaBTNodesMap['m'].right = alphaBTNodesMap['o']

alphaBTNodesMap['g'].left = alphaBTNodesMap['z']
alphaBTNodesMap['g'].right = alphaBTNodesMap['q']

alphaBTNodesMap['z'].left = None
alphaBTNodesMap['z'].rigth = None

alphaBTNodesMap['q'].left = None
alphaBTNodesMap['q'].rigth = None

alphaBTNodesMap['o'].left = None
alphaBTNodesMap['o'].right = None


print(decode_morse_code_helper(".-.", emptyRoot))