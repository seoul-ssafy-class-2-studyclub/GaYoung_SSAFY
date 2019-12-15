from heapq import heappop, heappush

numbers = int(input())
heap = []

for _ in range(numbers):
    num = int(input())
    heappush(heap, num)
    temp_heap = list(heap)
    for _ in range((len(temp_heap)+1)//2 - 1):
        heappop(temp_heap)
    print(temp_heap[0])