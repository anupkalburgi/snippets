class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# def path_sum(subtree, target_sum, acc_sum, path):
#     if subtree is None and target_sum == acc_sum:
#         return (True, acc_sum, path)
#     elif subtree is None:
#         return (False, acc_sum, path)
#     else:
#         (target_found, psl, lp) = path_sum(subtree.left, target_sum, acc_sum + subtree.val, path + [subtree.val] )
#         if target_found:
#             return (target_found, psl, lp)
#         else:
#             return path_sum(subtree.right, target_sum, acc_sum + subtree.val, path + [subtree.val])
            

#         # the thing seems wrong as we will have to sub stract what is there un acc_sum




def path_sum(subtree, target, acc_sum, path):
    if subtree is None:
        return (False, path)
    elif subtree.left is None and subtree.right is None and subtree.val + acc_sum  == target:
        return (True, path + [subtree.val])
    else:
        (lfnd , lpath) = path_sum(subtree.left, target , acc_sum + subtree.val, path + [subtree.val])
        (rfnd,  rpath) = path_sum(subtree.right, target ,acc_sum + subtree.val, path + [subtree.val])
        return (lfnd or rfnd, lpath if lfnd  else rpath)
            
root = TreeNode(5)

node4 = TreeNode(4)
node11 = TreeNode(11)
node7 = TreeNode(7)
node2 = TreeNode(2)

node8 = TreeNode(8)
node13 = TreeNode(13)
node4 = TreeNode(4)

root.left = node4
node4.left = node11
node11.left = node7
node11.right = node2

root.right = node8
node8.left = node13
node8.right = node4

print(path_sum(root,22, 0, []) )

