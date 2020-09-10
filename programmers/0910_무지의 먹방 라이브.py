food_times = [4, 3, 5, 6, 2]
k = 7

# food_times = [3, 1, 2]
# k = 5

# food_times = [1,1,1,1]
# k = 4

'''
[3, 1, 2] -> [2, 0, 1]로 한번에 가려면 len(food_times)만큼 건너뛰면 된다.
'''

from collections import deque

def solution(food_times, k):
    min_food_times = min(food_times)
    k -= len(food_times) * min_food_times

    q = deque([])
    for idx, num in enumerate(food_times):
        num -= min_food_times
        if num != 0:
            q.append([idx, num])
    print(q)
    if len(q) == 0:
        return -1
    else:
        k %= len(food_times)

print(solution(food_times,k))