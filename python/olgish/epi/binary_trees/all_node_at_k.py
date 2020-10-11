import typing

class TreeNode:
    def __init__(self, data):
        self.val = data
        self.left = None
        self.right = None
    def __str__(self):
        return str(self.val)

class Solution:
    mapping = {}

    def construct_child_to_parent_hash(self, subtree, parent):
        if subtree is None:
            return
        else:
            if parent is not None:
                self.mapping[str(subtree)] = parent
            self.construct_child_to_parent_hash(subtree.left, subtree)
            self.construct_child_to_parent_hash(subtree.right, subtree)


    # def construct_child_to_parent_hash(self, subtree: TreeNode):
    #     if subtree is None:
    #         return None
    #     else:
    #         self.mapping[subtree.left] = subtree
    #         self.mapping[subtree.right] = subtree
    #         self.construct_child_to_parent_hash(subtree.left)
    #         self.construct_child_to_parent_hash(subtree.right)
            

            # l = self.construct_child_to_parent_hash(subtree.left)
            # r = self.construct_child_to_parent_hash(subtree.right)
            # if l:
            #     self.mapping[l] = subtree
            # if r:
            #     self.mapping[r] = subtree
            # return subtree


    # def bfs(subtree: TreeNode, visited: set, depth: int, tovisit: list):
    #     if tovisit is None:
    #         return tovisit
    #     if depth == 0:
    #         return subtree
    #     (np, nl, nr) = (self.mapping[subtree], subtree.left, subtree.right)
    #     depth =  depth - 1
    #     p = self.bfs(np)
    #     l = self.bfs(nl)
    #     r = self.bfs(nl)



    def nodes_at_dist_k(self, root: TreeNode, target: TreeNode, dist: int):
        queue = []
        visited = []
        depth_cnt = 0 
        self.construct_child_to_parent_hash(root, None)
        print(self.mapping)

        queue.append(target)
        visited.append(target)
        while queue and depth_cnt <= dist:
            qsize = len(queue)
            depth_cnt =  depth_cnt + 1
            for _ in range(0, qsize):
                node = queue.pop(0)
                if str(node) in self.mapping:
                    np = self.mapping[str(node)]
                    visited.append(np)
                    queue.append(np)
                (nl, nr) =  (node.left, node.right)
                if nr not in visited:
                    visited.append(nr)
                    queue.append(nr)
                if nl not in visited:
                    visited.append(nl)
                    queue.append(nl)
        return queue


            
            


        # return self.find_node(root, target)
# when adding it a queue mark it visited
root = TreeNode(6)
node3 = TreeNode(3)
node8 = TreeNode(8)
node9 = TreeNode(9)
node4 = TreeNode(4)

root.left = node3
root.right = node4

node3.left = node8
node3.right = node9

sol = Solution()
sol.construct_child_to_parent_hash(root, None)
print(str(sol.mapping))
print(sol.nodes_at_dist_k(root, node3, 1))
# print(str(sol.nodes_at_dist_k(root, node3, 1)))



# construct a dict of child to parent 
# using bfs to solve the problem which involves using a visited hashset/set