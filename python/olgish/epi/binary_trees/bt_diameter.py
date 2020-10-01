class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None



# Idea is get all the paths then return the max of the paths

def paths(subtree):
    if subtree is None:
        return [[]]
    elif subtree.left is None and subtree.right is None:
        return [[subtree.val]]
    else:
        lpaths = paths(subtree.left)
        rpaths = paths(subtree.right)

        tst = [subtree.val] + lpaths + rpaths
        print(f"testing {tst} ---  ll: {lpaths} -- r: {rpaths} ")
        
        return [ [subtree.val] + p for p in lpaths] + [ [subtree.val] + p for p in rpaths]
        
        # return paths(subtree.left) + [subtree.val] + paths(subtree.right)
        # this will not work as we are interested in finding boths ways and not just one

        # return paths(subtree.left, all_paths , current_path + [subtree.val]) + paths(subtree.right, all_paths, current_path + [subtree.val])
        # this will not work as we are getting paths from root to all the node, but we will have to find a way to merge them


class Dumb:
    max_path = 4

    def max_path_length(self,subtree):
        if subtree is None:
            return 0
        else:
            l = self.max_path_length(subtree.left)
            r = self.max_path_length(subtree.right)
            if (l + r + 1) > self.max_path:
                self.max_path = l + r + 1 
        return max(l + 1, r + 1)


        # max_path_length(A) {
        #     l = max_path_length(B) 
        #         {
        #                 l = {
        #                     max_path_length(E)
        #                         max_path_length(None)
        #                     l = 0
        #                         max_path_length(None)
        #                     r = 0
        #                     max_path =  1
        #                 } = 1

        #                 r = {
        #                     max_path_length(F)
        #                         max_path_length(None)
        #                     l = 0 
        #                         max_path_length(None)
        #                     r = 0
        #                     max_path # no change
        #                     max()
        #                 } = 1
        #             max_path = 3
        #         }    
        #          = 2
        #     r = max_path_length(c)
        #             { l = max_path_length(None)
        #                 0
        #             r = max_path_length(None)
        #                 0
        #             max_path # no change
        #             }  = 1
        #         max_path = 4
        # } =  3
        # # 

        # return max_path - 1 

root = TreeNode(1)
node2 = TreeNode(2)
node4 = TreeNode(4)
node5 = TreeNode(5) 
node3 = TreeNode(3)

root.left = node2
node2.left = node4
node2.right = node5

root.right = node3


d = Dumb()
print(d.max_path)