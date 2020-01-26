'''
1. 최대 힙(max heap)
   : 부모 노드의 키 값이 자식 노드의 키 값보다 크거나 같은 완전 이진 트리
     key(부모 노드) >= key(자식 노드)

2. 최소 힙(min heap)
   : 부모 노드의 키 값이 자식 노드의 키 값보다 작거나 같은 완전 이진 트리
     key(부모 노드) <= key(자식 노드)
'''

from heapq import heappush, heappop

N = int(input())
number_l = []
number_r = []

