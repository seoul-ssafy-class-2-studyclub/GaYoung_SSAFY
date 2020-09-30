'''
1. 트리를 순회하는 방법은 검색을 통해 쉽게 알 수 있으므로 문제가 되지 않습니다.
2. 이 문제의 핵심은 좌표 값으로 주어지는 노드들을 트리로 구성하는 부분입니다.
3. 트리를 만들기 위해 y값을 이용해서 각 노드의 level을 분리하고,
   현재 노드의 자식노드가 가질 수 있는 x값을 이용해서 현재노드의 왼쪽, 오른쪽 자식을 정확하게 찾는 것이 중요하다
4. 각 노드의 왼쪽, 오른쪽 자식노드 찾기
  - 먼저 노드 P의 x의 값을 Px, 현재노드의 자식노드가 가질 수 있는 x의 범위를 Lx, Rx(Lx < Px < Rx)
  - 또 어떤 노드 K의 x값을 Kx -> 만약 현재 노드의 바로 다음 레벨에 Lx ≤ Kx < Px를 만족하는 노드 K가 있으면 -> K는 노드 P의 왼쪽 자식
  - 노드 K의 자식 노드가 가질 수 있는 x값의 범위 : Lx ≤ x ≤ Px – 1 (x ≠ Kx)
  - 현재 노드의 바로 다음 레벨에 Px < Kx ≤ Rx를 만족하는 노드 K -> Px + 1 ≤ x ≤ Rx (x ≠ Kx)
5. 위 과정을 재귀적으로 반복하면서 각 노드의 왼쪽, 오른쪽 자식을 찾아주면 트리를 구성할 수 있습니다.

6. 노드별 왼쪽, 오른쪽 자식을 찾는 방법
  - 재귀적으로 순회하며 트리를 만들면 같은 level의 노드는 x값이 작은 노드부터 방문
  - 큐를 트리의 레벨만큼 만들어 두고, x축 기준으로 오름차순 정렬된 노드들을 y축 값이 같은 노드끼리 각 큐에 넣어두면 큐의 front를 확인하는 방법으로 O(1)에 찾을 수 있
  - 트리를 구성:O(N), 시간 복잡도 : O(NlogN)
'''

nodeinfo = [[5,3],[11,5],[13,3],[3,5],[6,1],[1,3],[8,6],[7,2],[2,2]]

# 재귀함수 사용시 필수!!
import sys

sys.setrecursionlimit(10 ** 6)

class Tree:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

preorder = []
postorder = []

'''
[순회]
1. 전위순회(Preorder Traversal) : root - left - right
2. 중위순회(Inorder Traversal) : left - root - right
3. 후위순회(Postorder Traversal) : left - right - root
'''
def make_preorder(node, nodeinfo):
    preorder.append(nodeinfo.index(node.data) + 1)

    if node.left:
        make_preorder(node.left, nodeinfo)
    if node.right:
        make_preorder(node.right, nodeinfo)

def make_postorder(node, nodeinfo):
    if node.left:
        make_postorder(node.left, nodeinfo)
    if node.right:
        make_postorder(node.right, nodeinfo)

    postorder.append(nodeinfo.index(node.data) + 1)

def solution(nodeinfo):

    # [x,y] : y=level인데 y가 높을수록 부모노드, x는 같은부모노드에서 작으면 left, 크면 right
    sort_nodeinfo = sorted(nodeinfo, key=lambda x: (-x[1], x[0]))
    # [[8, 6], [3, 5], [11, 5], [1, 3], [5, 3], [13, 3], [2, 2], [7, 2], [6, 1]]

    root = None
    for node in sort_nodeinfo:
        if not root:  # root == None:
            root = Tree(node)
            # nodeinfo = [[8, 6], [3, 5], [11, 5], [1, 3], [5, 3], [13, 3], [2, 2], [7, 2], [6, 1]]
        else:
            current = root
            # root를 찾고 남은 node들은 root부터 시작해서 x좌표를 비교해서 이 값이 left인지 right인지 확인
            # 만약, 현재 node에서 이미 left나 right값이 있다면, 그 노드로 이동해서 다시 비교하고 지정해줌
            # 얼마나 반복해야할지 몰라서 while사용했고, 연결완료하면 break
            while True:
                if node[0] < current.data[0]:
                    if current.left:
                        current = current.left
                        continue
                    else:
                        current.left = Tree(node)
                        break


                if node[0] > current.data[0]:
                    if current.right:
                        current = current.right
                        continue
                    else:
                        current.right = Tree(node)
                        break

                break

    make_preorder(root, nodeinfo)
    make_postorder(root, nodeinfo)
    return [preorder, postorder]

print(solution(nodeinfo))