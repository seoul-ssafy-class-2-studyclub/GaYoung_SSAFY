from itertools import combinations

def connect(array):
    arr = array[:]
    # print(arr)
    if len(arr) == 1:
        return True
    else:
        q = [arr[0]]
        while q:
            node = q.pop(0)
            # node가 arr안에 있으면 arr에서 삭제
            if node in arr:
                arr.remove(node)
                # adj의 node번째에 들어가서 다음 값이 arr에 있다면, q에 추가
                for nxt in adj[node]:
                    if nxt in arr:
                        q.append(nxt)

        # 모든 값들이 node로 pop이 되면 arr에 들어있는 것들이 줄어듦
        if len(arr) == 0:
            return True
        else:
            return False

N = int(input())
population = list(map(int, input().split()))
adj = [[] for _ in range(N)]
all_pop = sum(population)

for i in range(N):
    data = list(map(int, input().split()))
    for j in range(data[0]):
        adj[i].append(data[j + 1] - 1)
'''
6
5 2 3 4 1 2
2 2 4
4 1 3 6 5
2 4 2
2 1 3
1 2
1 2

답1

8
17 42 46 81 71 8 37 12
4 2 4 5 7
5 1 3 4 5 8
2 2 4
5 1 2 3 7 8
5 1 2 6 7 8
2 5 8
4 1 4 5 8
5 2 4 5 6 7
답 2

6
2 2 2 2 2 2
1 3
1 4
1 1
1 2
1 6
1 5
답-1
'''

inf = float('inf')
mymin = inf
for i in range(1, N // 2 + 1):
    result = list(combinations(list(range(N)), i))
    for a in result:
        a = list(a)
        if connect(a) == False:
            continue
        else:
            b = list(set(range(N)) - set(a))
            if connect(b) == False:
                continue
            else:
                sum_b = 0
                for k in b:
                    sum_b += population[k]
                sum_a = all_pop - sum_b
                diff = abs(sum_a - sum_b)
                if mymin > diff:
                    mymin = diff

if mymin == inf:
    print(-1)
else:
    print(mymin)