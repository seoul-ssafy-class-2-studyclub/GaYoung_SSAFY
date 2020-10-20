# operations = ['I 16','D 1']
operations = ['I 7','I 5','I -5','D -1']

import heapq

def solution(operations):
    heap = []
    for operation in operations:
        word, num = operation.split(' ')

        if word == 'I':
            heapq.heappush(heap, int(num))

        else:
            if heap:
                if num == '1':
                    heap.remove(max(heap))
                else:
                    heapq.heappop(heap)

    if not heap:
        return [0, 0]

    return [max(heap), min(heap)]

print(solution(operations))