class _BinaryTree:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
    def __str__(self):
        return self.data
    
def preorder(subtree: _BinaryTree):
    if subtree is not None:
        print(subtree.data)
        preorder(subtree.left)
        preorder(subtree.right)

def inorder(subtree: _BinaryTree):
    if subtree is not None:
        inorder(subtree.left)
        print(subtree.data) # visit op
        inorder(subtree.right)

def postOrder(subtree: _BinaryTree):
    if subtree is not None:
        postOrder(subtree.left)
        postOrder(subtree.right)
        print(subtree.data)

def bfs(subtree: _BinaryTree):
    qu = []
    qu.append(subtree)

    while qu:
        node = qu.pop(0)
        print(node.data)
        if node.left:
            qu.append(node.left)
        if node.right:
            qu.append(node.right)

def bTree_by_level(root):
    levels = []
    ans = []


    def children_at_level(nodes):
        children = []
        for node in nodes:
            if node.left:
                children.append(node.left)
            if node.right:
                children.append(node.right)
        return children


    # we know root we start from:
    # next_levl_child.append() # [5,3]

    ans.append([root.data])
    levels.append([root]) # [[Node(A)]]
    while levels:
        level = levels.pop(0) # level =  [[Node(B), Node(C)]] levels = []
        nex_chd = children_at_level(level) # [Node(D), Node(E), Node(F), Node(G)]
        next_ans = []
        for chld in nex_chd:
            next_ans.append(str(chld))
        ans.append(next_ans)
        if nex_chd:
            levels.append(nex_chd) # levels = [[Node(D), Node(E), Node(F), Node(G)]]


    

    return ans



        

bta  = _BinaryTree("A")
btb = _BinaryTree("B")
btd = _BinaryTree("D")
bte = _BinaryTree("E")
bth = _BinaryTree("H")
btc = _BinaryTree("C")
btf = _BinaryTree("F")
btg = _BinaryTree("G")
bti = _BinaryTree("I")
btj = _BinaryTree("J")

bta.left = btb
bta.right = btc

btb.left = btd
btb.right = bte
bte.left = bth


btc.left = btf
btc.right = btg

btg.left = bti
btg.right = btj

# bfs(bta)

print("----------------------------")
print(bTree_by_level(bta))






    