import ast
from pprint import pprint
from ast import NodeVisitor


def main():
    with open("/Users/anupkalburgi/projects/snippets/python/sample.py", "r") as source:
        tree = ast.parse(source.read())

    analyzer = Analyzer()
    analyzer.visit(tree)
    analyzer.report()


class Analyzer(ast.NodeVisitor):
    def __init__(self):
        self.stats = {"import": [], "from": [], "class": []}

    def visit_Import(self, node):
        for alias in node.names:
            self.stats["import"].append(alias.name)
        self.generic_visit(node)

    def visit_ImportFrom(self, node):
        for alias in node.names:
            self.stats["from"].append(alias.name)
        self.generic_visit(node)

    def visit_ClassDef(self, node):
        print(node.name)
        # if bases have luigi class then add them to the list
        for base in node.bases:
            if isinstance(base, ast.Name):
                self.stats["class"].append(base.id)
            elif isinstance(base, ast.Attribute):
                self.stats["class"].append(base.attr)
        self.generic_visit(node)

    def report(self):
        pprint(self.stats)


if __name__ == "__main__":
    main()
