import typing

class TreeNode:
    def __init__(self, data):
        self.val = data
        self.left = None
        
        self.right = None
class Solution:
    pairs = []
    def all_root_pairs(self, subtree: TreeNode):
        if subtree is None:
            return []
        else:
            lt = self.all_root_pairs(subtree.left)
            rt = self.all_root_pairs(subtree.right)
            for r in rt:
                self.pairs.append((subtree.val , r))
            for l in lt:
                self.pairs.append((subtree.val, l))
            return [subtree.val] + lt + rt

    def max_abs_diff(self, root):
        self.all_root_pairs(root)
        return max(map(lambda x: abs(x[0] - x[1]), self.pairs))
    
root = TreeNode(8)
node3 = TreeNode(3)
node1 = TreeNode(1)
node6 = TreeNode(6)
node4 = TreeNode(4)
node7 = TreeNode(7)
node10 = TreeNode(10)
node14 = TreeNode(14)
node13 = TreeNode(13)

root.left = node3
node3.left = node1
node3.right = node6

node6.left = node4
node6.right = node7
node10.right = node14

root.right = node10
node14.left = node13

sol = Solution()

print(sol.max_abs_diff(root))