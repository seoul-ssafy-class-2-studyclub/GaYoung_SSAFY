'''
[heap 구조]
1. 개념
 - 최댓값과 최솟값을 빠르게 찾기 위해 고안된 자료구조
 - 각 노드의 key값이 해당 노드의 자식노드의 key값보다 작지 않거나 크지 않은 완전 이진트리
 - 키 값의 대소관계는 부모-자식 노드 사이 간에만 성립하며 형제 노드 사이에는 영향을 미치지 않음
 - 자식노드의 최대 개수는 힙의 종류에 따라 다르지만 이진트리에서는 최대 2개
 - i번째 노드의 자식노드가 2개인데 왼쪽 자식노드는 2i, 오른쪽 자식노드는 2i+1이고, 부모노드는 i/2가 된다.

2. 최대 힙 (max heap), 최소 힙 (min heap)
 - 최대 힙: 각 노드의 키 값이 그 자식노드의 키 값보다 작지 않은 힙
 - 최소 힙: 각 노드의 키 값이 그 자식노드의 키 값보다 크지 않은 힙

3. 시간복잡도: O(log n)

4. 삽입 연산 (insertion)
 - 삽입하고자 하는 값을 트리의 가장 마지막 원소에 추가한다.
 - 부모노드와의 대소관계를 비교하면서 만족할 때까지 자리 교환을 반복한다.

5. 삭제 연산 (deletion)
 - 힙에서는 루트 노드만 삭제가 가능하므로 루트 노드를 제거한다.
 - 가장 마지막 노드를 루트로 이동시킨다.
 - 자식노드와 비교하여 조건이 만족할 때까지 이동시킨다.


 -
 -
 -
 -
 -
 -
 -
 -
 -
'''


# 최대 힙 만들기
import heapq

# nums = [4, 1, 7, 3, 8, 5]
# heap = []
#
# for num in nums:
#     heapq.heappush(heap, (-num, num))  # (우선 순위, 값)
#     print(heap)
#
# while heap:
#     print(heapq.heappop(heap))
# #   print(heapq.heappop(heap)[1])  # index 1

temp = []
heapq.heappush(temp, 4)
print(temp)
heapq.heappush(temp, 1)
print(temp)
heapq.heappush(temp, 7)
print(temp)
heapq.heappush(temp, 3)
print(temp)
heapq.heappush(temp, 8)
print(temp)
heapq.heappush(temp, 5)
print(temp)

# ls = [4, 1, 7, 3, 8, 5]
# heapq.heapify(ls)
# print(ls)