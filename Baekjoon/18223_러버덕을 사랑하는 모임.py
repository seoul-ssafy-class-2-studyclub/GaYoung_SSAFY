from itertools import combinations

N, P, E = map(int, input().split())

all = []
for n in range(N):
    x, y = map(int, input().split())
    all.append((x, y))
print(all)  #[(10, 20), (15, 16), (1, 8), (17, 22), (2, 3)]

num = [n for n in range(N)]
result = list(combinations(num, P))
print(result)  # [(0, 1), (0, 2), (0, 3), (0, 4), (1, 2), (1, 3), (1, 4), (2, 3), (2, 4), (3, 4)]

for r in range(len(result)):
    mymin = 999999999999999999999
    mymax = 0
    for p in range(P):
        mymin = sum(all[r[p]][0])
        mymax = sum(all[r[p]][1])

