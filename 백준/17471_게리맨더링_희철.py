import itertools

def is_connected(array):
    arr = array[:]
    if len(arr) == 1:
        return True
    else:
        queue = [arr[0]]

        while queue:
            node = queue.pop(0)
            if node in arr:
                arr.remove(node)
                for nxt in board[node]:
                    if nxt in arr:
                        queue.append(nxt)

        if len(arr) == 0:
            return True
        else:
            return False


N = int(input())
population_list = list(map(int, input().split()))
total = sum(population_list)

board = [[] for _ in range(N)]
inf = float('inf')
min_gap = inf

for i in range(N):
    temp = list(map(int, input().split()))
    for j in range(temp[0]):
        board[i].append(temp[j + 1] - 1)

for k in range(1, N // 2 + 1):
    comb_all_a = list(itertools.combinations(list(range(N)), k))
    print(comb_all_a)

    for district_a in comb_all_a:
        if is_connected(list(district_a)) is False:
            continue
        else:
            district_b = list(set(range(N)) - set(district_a))
            if is_connected(district_b) is False:
                continue
            else:
                people_b = 0
                for i in district_b:
                    people_b += population_list[i]

                gap = abs(total - 2 * people_b)
                if min_gap > gap:
                    min_gap = gap
                    continue


if min_gap == inf:
    print(-1)
else:
    print(min_gap)