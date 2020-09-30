'''
이진트리 = 분할정복 탐색 알고리즘

[순회]
1. 전위순회(Preorder Traversal) : root - left - right
2. 중위순회(Inorder Traversal) : left - root - right
3. 후위순회(Postorder Traversal) : left - right - root
'''

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def init_tree():
    global root

    new_node = Node('A')
    root = new_node

    new_node = Node('B')
    root.left = new_node
    new_node = Node('C')
    root.right = new_node

    new_node1 = Node('D')
    new_node2 = Node('E')
    node = root.left
    node.left = new_node1
    node.right = new_node2

    new_node1 = Node('F')
    new_node2 = Node('G')
    node = root.right
    node.left = new_node1
    node.right = new_node2


def preorder(node):
    if node == None: return
    print(node.data, end='->')
    preorder(node.left)
    preorder(node.right)

    if __name__ == "__main__":
        preorder(root)