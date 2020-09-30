# 클래스 정의 및 초기화
class Node(object):
    def __init__(self, data):
        self.data = data
        self.left = self.right = None

# BinarySearchTree를 구현 -> 처음에는 비어있는 트리로 초기화
class BinarySearchTree(object):
    def __init__(self):
        self.root = None

    # 삽입 : 리에 새 원소를 추가(재귀이용)
    def insert_value(self, node, data):
        if node is None:
            node = Node(data)

        else:
            if data <= node.data:  # left로 감
                node.left = self.insert_value(node.left, data)
            else:
                node.right = self.insert_value(node.right, data)

        return node

    # 탐색 : 원하는 값의 존재유무를 확인
    def find(self, key):
        return self.find_value(self.root, key)

    def find_value(self, root, key):
        if root is None or root.data == key:
            return root is not None

        elif key < root.data:
            return self.find_value(root.left, key)

        else:
            return self.find_value(root.right, key)

    # 삭제
    # 삭제노드 1개 = 그냥 하나 가지고오면 된다.
    # 삭제노드 2개 = 왼쪽 서브 트리와 오른쪽 서브 트리를 각각 A, B라고 했을 때,
    #              B에서 가장 왼쪽 아래에 위치한 자손을 가져온다.
    #              (A의 모든 원소보다는 크면서 B의 나머지원소보다는 작기 때문)
    def delete(self, key):
        self.root, deleted = self.delete_value(self.root, key)
        return deleted

    # 이해안됨
    def delete_value(self, node, key):
        if node is None:
            return node, False

        deleted = False
        if key == node.data:
            deleted = True
            if node.left and node.right:
                parent, child = node, node.right
                while child.left is not None:
                    parent, child = child, child.left
                child.left = node.left
                if parent != node:
                    parent.left = child.right
                    child.right = node.right
                node = child
            elif node.left or node.right:
                node = node.left or node.right
            else:
                node = None
        elif key < node.data:
            node.left, deleted = self.delete_value(node.left, key)
        else:
            node.right, deleted = self.delete_value(node.right, key)
        return node, deleted
