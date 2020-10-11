class TreeNode:
    def __init__(self, data):
        self.val = data
        self.left = None 
        self.right = None           

# def all_paths(subtree: TreeNode):
#     if subtree is None:
#         return [[]]
#     # if subtree.left is None and subtree.right is None:
#         # return 
#     else:
#         lp = all_paths(subtree.left)             
#         rp = all_paths(subtree.right)
#         llp = [ [subtree.val] + l for l in lp]
#         rrp = [ [subtree.val] + r for r in rp] 
        # return llp + rrp

def all_path_tail(subtree: TreeNode, all_path_acc, curr_path):
    if subtree is None:
        return all_path_acc + [curr_path]
    if subtree.left is None and subtree.right is None:
        return  all_path_acc + [ curr_path + [subtree.val]] 
    else:
        lp = all_path_tail(subtree.left, all_path_acc,  curr_path + [subtree.val]   )
        rp = all_path_tail(subtree.right, all_path_acc,  curr_path + [subtree.val]  )
        return  lp + rp 


root = TreeNode(8)
node6 = TreeNode(6)
node5 = TreeNode(5)
node3 = TreeNode(3)
node10 = TreeNode(10)
node12 = TreeNode(12)

root.left = node6
root.right = node10

node6.left = node5
node6.right = node3

node10.left = node12

# # print(all_paths(root))

a_paths = all_path_tail(root, [], [])
print(a_paths)
# fl = a_paths.pop(0)
# rst = [p[-1] for p in a_paths]
# print([fl] + rst)