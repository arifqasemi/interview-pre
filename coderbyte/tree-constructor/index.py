class TreeNode:
    def __init__(self,node_value):
        self.value = node_value
        self.children = []
        
    def add_child(self,value):
        self.children.append(value)
        
    def __str__(self):
        return self.value
    
    
    
root = TreeNode('A')

b = TreeNode('B')
c = TreeNode('C')

root.add_child(b)
root.add_child(c)

d = TreeNode('D')
b.add_child(d)
print(d)
# def print_tree(node, level=0):
#     print("  " * level + str(node.value))
#     for child in node.children:
#         print_tree(child, level + 1)

# print_tree(root)

