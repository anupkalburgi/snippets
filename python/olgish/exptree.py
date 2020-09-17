class _ExprTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class ExpressionTree:
    def __init__(self, exprStr):
        self._expTree: _ExprTreeNode = None
        self._buildTree(exprStr)

    def _buildTree(self, exprStr):
        q = []
        for elm in exprStr:
            q.append(elm)
        self._expTree = _ExprTreeNode(None)
        return self._recBuildTree(self._expTree, q)
        

    def _recBuildTree(self, currNode, exq):
        token = exq.pop(0)
        # Base case occurs when the q is empty
        if token == "(":
            currNode.left = _ExprTreeNode(None)
            self._recBuildTree(currNode.left, exq)
            # next element must be a operator +, -, /

            operator = exq.pop(0)
            currNode.data = operator
            # next element must be a operator
            currNode.right = _ExprTreeNode(None)
            self._recBuildTree(currNode.right, exq)
            # next must be a closing param
            exq.pop(0)
        else:
            # There should be a number
            currNode.data = token
    
    def evaluate(self):
        return self._evalTree(self._expTree)

    def _evalTree(self, currNode):
        if currNode.left is None and currNode.right is None:
            return int(currNode.data)
        else:
            # Must be a operator node
            left_value = self._evalTree(currNode.left)
            right_value = self._evalTree(currNode.right)
            # actually currNode is Operation
            return self.computeOp(currNode.data, left_value, right_value)

    def computeOp(self, op, left, right):
        if op == "+":
            return left + right
        elif op == "*":
            return left * right
        elif op == "/":
            return left / right
        elif op == "%":
            return left % right
        else:
            "you crazy"


    
    def __str__(self):
        return self._buildString(self._expTree)

    def _buildString(self, treeNode: _ExprTreeNode):
        if treeNode.left is None and treeNode.right is None:
            return str(treeNode.data)
        else:
            exprStr = "( "
            exprStr += self._buildString(treeNode.left)
            exprStr += treeNode.data
            exprStr += self._buildString(treeNode.right)
            exprStr += " )"
            return exprStr



exT = ExpressionTree("((2*7)+8)")
print(str(exT))
print(exT.evaluate())