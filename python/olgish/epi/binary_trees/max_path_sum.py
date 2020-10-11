class TreeNode:
    def __init__(self, data):
        self.val = data
        self.left = None
        self.right = None
    
class Sol:
    maximim_sum = -999999

    def max_sum_bt(self, subtree):
        if subtree is None:
            return 0
        else:
            l = max(self.max_sum_bt(subtree.left), 0)
            r = max(self.max_sum_bt(subtree.right), 0)
            self.maximim_sum = max(self.maximim_sum, l + r + subtree.val)
            return max(subtree.val + r , subtree.val + l)
        # else:
        #     l = self.max_sum_bt(subtree.left)
        #     r = self.max_sum_bt(subtree.right)
        #     if (l + r + subtree.val) > self.maximim_sum:
        #         self.maximim_sum = l + r + subtree.val
            
        #     return max(subtree.val + l, subtree.val + r)

# root = TreeNode(-10)

# node9 = TreeNode(9)
# node20 = TreeNode(20)
# node15 = TreeNode(15)
# node7 = TreeNode(7)

# root.left = node9
# root.right = node20

# node20.left = node15
# node20.right = node7

root = TreeNode(2)
noden1 = TreeNode(-1)
noden2 = TreeNode(-2)
root.left = noden1
root.right = noden2
s = Sol()
lrmax = s.max_sum_bt(root)
print(lrmax)
print(s.maximim_sum)

