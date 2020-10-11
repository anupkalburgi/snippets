class TreeNode:
    def __init__(self, data):
        self.val = data
        self.left = None
        self.right = None


class Sol:
    child_to_parent  = {}

    def constuct_parent_mapping(self, subtree, parent):
        if subtree is None:
            return
        else:
            if parent is not None:
                self.child_to_parent[subtree.val] = parent
            self.constuct_parent_mapping(subtree.left, subtree.val)
            self.constuct_parent_mapping(subtree.right, subtree.val)

    def get_node_at_dist(self, subtree, dist, nodes):
        if dist == 0:
            return nodes
        if subtree is None:
            return []
        else:
            l = self.get_node_at_dist(subtree.left, dist - 1, nodes + [subtree])
            r = self.get_node_at_dist(subtree.right, dist -1, nodes + [subtree])
            return l + r 
    
    def node_at_dist_k(self, root, target, dist):
        # Have to return a list of node at distance k
        self.constuct_parent_mapping(root, None) # generally a code smell
        visited = [target]
        q = [target]
        # Have to do getting the parent till dist is zero
        # Challange how do we cross over the root, 
        # have to either go left or right
        # so will have to maintain a visited set
        # But then we might have to go in both left and right, so we also need a queue
        while dist > 0 and q:
            qsize = len(q)
            for _ in range(qsize):
                node = q.pop(0)
                if node.val in self.child_to_parent:
                    if node not in visited:
                        q.append(node)
                        visited.append(node)
                (lp, rp) = (node.left, node.right)
                if lp not in visited:
                    visited.append(lp)
                    q.append(lp)
                if rp not in visited:
                    visited.append(rp)
                    q.append(rp)
            dist = dist  - 1
        res = []
        for n in q:
            res.append(n.val)
        return res


    
root = TreeNode(3)
node5 = TreeNode(5)
node6 = TreeNode(6)
node2 = TreeNode(2)
node7 = TreeNode(7)
node4 = TreeNode(4)
node1 = TreeNode(1)
node0 = TreeNode(0)
node10 = TreeNode(10)
node11  = TreeNode(11)

root.left = node5
root.right = node1

node5.left = node6
node5.right = node2

node2.left = node7
node2.right = node4
node1.left = node0
node1.right = node11

sol = Sol()
sol.constuct_parent_mapping(root, None)
print(sol.child_to_parent)

'''
first walk the tree and construct a reverse map of child to parent
{
    child -> Parent
}

once that is in place we can traverse the dict and get all the node at dist k
or we can walk the tree and get the target node first and do a dfs and get the path there 
and then was walk a dict
'''
