import ast
class Foo:
    def __init__(self, val):
        self.value = val

class Bar(Foo):
    def __init__(self, name):
        self.instance_name = name

class AstThingAain(ast.NodeVisitor):
    def __init__(self, tree):
        self.file_name = tree
