import ast
with open('18/input.txt', 'r') as reader:
    lines = [line.strip() for line in reader if line.strip()]


class Transformer(ast.NodeTransformer):
    def visit_Sub(self, node):
        return ast.Mult()


result = 0
for line in lines:
    tree = ast.parse(line.replace("*", "-"), mode='eval')
    tranformed_tree = Transformer().visit(tree)
    value = eval(compile(tranformed_tree, '', mode='eval'))
    result += value
    # print(value)

print(result)
