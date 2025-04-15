import ast
import graphviz

class ExpressionTree:
    def __init__(self, root):
        self.root = root

    def visualize(self):
        dot = graphviz.Digraph()
        self._add_nodes(dot, self.root)
        dot.render('arbol_expresion', view=True)

    def _add_nodes(self, dot, node):
        if isinstance(node, ast.BinOp):
            dot.node(str(id(node)), self._get_operator(node.op))
            dot.edge(str(id(node)), str(id(node.left)))
            dot.edge(str(id(node)), str(id(node.right)))
            self._add_nodes(dot, node.left)
            self._add_nodes(dot, node.right)
        elif isinstance(node, ast.Num):
            dot.node(str(id(node)), str(node.n))

    def _get_operator(self, op):
        if isinstance(op, ast.Add):
            return '+'
        elif isinstance(op, ast.Sub):
            return '-'
        elif isinstance(op, ast.Mult):
            return '*'
        elif isinstance(op, ast.Div):
            return '/'
        elif isinstance(op, ast.Pow):
            return '**'
        return ''

def build_expression_tree(expression):
    parsed_expression = ast.parse(expression, mode='eval')
    return ExpressionTree(parsed_expression.body)

if __name__ == "__main__":
    expression = "3 * (9 - 3 * 4)"
    tree = build_expression_tree(expression)
    tree.visualize()