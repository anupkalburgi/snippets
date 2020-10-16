# there are three possible situation here
# 1. left < root < right - then root is the answer as going doing either direction is going to increase the diff
# 2. target < root.val go left
# 3. target > right.val go right
# here we cannot use zero as  the base condition as we will have to check of both left and right are none and return accordingly


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def close(self, subtree, target, closest):
        if subtree is None:
            return closest
        else:
            if subtree.val == target:
                return subtree.val
            else:
                nclose = abs(subtree.val - target)
                if nclose < abs(closest - target):
                    closest = subtree.val
                if subtree.val < target:
                    return self.close(subtree.right, target, closest)
                else:
                    return self.close(subtree.left, target, closest)

        
    def closestValue(self, root: TreeNode, target: float) -> int:
        if root is None:
            return None
        return self.close(root, target, root.val)
# 3.28