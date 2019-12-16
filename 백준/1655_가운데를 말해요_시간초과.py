from heapq import heappop, heappush

numbers = int(input())
arr = []

cnt = 0
for _ in range(numbers):
    num = int(input())
    heappush(arr, num)
    arr_list = list(arr)
    cnt += 1
    for _ in range((len(arr_list)+1)//2 - 1):
        heappop(arr_list)
    print(arr_list[0])