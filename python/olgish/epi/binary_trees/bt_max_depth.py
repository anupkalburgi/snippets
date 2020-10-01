class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None



def height(subtree, all_paths, current_path):
    if subtree is None:
        return all_paths
    elif subtree.left is None and subtree.right is None:
        return all_paths + [current_path + [subtree.val]]
    else:
        return height(subtree.left, all_paths, current_path + [subtree.val]) + height(subtree.right, all_paths, current_path + [subtree.val]) 

def max_depth(root):
    if root is None:
        return 0
    else:
        all_paths = height(root, [], [])
        print(all_paths)
        return max( map(lambda lst: len(lst), all_paths))


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

print(max_depth(root))