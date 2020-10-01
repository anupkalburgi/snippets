class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def lca(root, p, q):
    if root.val == p.val or root.val == q.val:
        return root.val
    elif root.val > p.val and root.val > q.val:
        return lca(root.left, p, q)
    elif root.val < p.val and root.val < q.val:
        return lca(root.right, p, q)
    else: # this is becasue one is on to left and the other on right
        return root.val
    
    



broot = TreeNode(6)
node2 =  TreeNode(2)

node0 =  TreeNode(0)
node4 =  TreeNode(4)
node3 =  TreeNode(3)
node5 =  TreeNode(5)

node8 =  TreeNode(8)
node7 =  TreeNode(7)
node9 =  TreeNode(9)


broot.left = node2

node2.left = node0
node2.right = node4

node4.left = node3
node4.right = node5

broot.rigth = node8

node8.left = node7
node8.right = node9

print(lca(broot, TreeNode(2), TreeNode(8) ))