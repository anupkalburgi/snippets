class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def height(subtree):
    if subtree is None:
        return 1
    else:
        lh = height(subtree.left)
        rh = height(subtree.right)
        return( 1 + lh + rh)

def is_balanced(root):
    if root is None:
        return True
    lh = height(root.left)
    rh = height(root.right)
    if abs(lh - rh) >= 1:
        return True
    else:
        return False

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

print(is_balanced(broot))