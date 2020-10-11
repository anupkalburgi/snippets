class TreeNode:
    def __init__(self, data):
        self.val = data
        self.left = None
        self.right = None


def max_depth_top_down(subtree, max_depth, current_depth):
    # basically we on null we have return the answerm, and the answer has to be the biger of what we knew earlier vs the path that we have now
    if subtree is None:
        return max(max_depth, current_depth)
    else:
        return max(max_depth_top_down(subtree.left, max_depth, current_depth + 1) , max_depth_top_down(subtree.right, max_depth, current_depth +1))

def max_depth_bottom_up(subtree):
    if subtree is None:
        return 0
    else:
        return max(1 + max_depth_bottom_up(subtree.left) , 1+ max_depth_bottom_up(subtree.right))


root = TreeNode(15)

node6 = TreeNode(6)
node2 = TreeNode(2)
node0 = TreeNode(0)
node18 = TreeNode(18)
node17 = TreeNode(17)
node16 =TreeNode(16)

root.left = node6
root.right = node18

node6.left = node2
node6.right = node17

node2.left = node0

node18.left = node17
node18.right = node16

print(max_depth_top_down(root, 0, 0))
print(max_depth_bottom_up(root))