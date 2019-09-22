N = int(input())
data = list(map(int, input().split()))

idx = []  # [0, 2, 6]
for i in range(N):
    if data[i] == 1:
        idx.append(i)

seat = 0
dis = []
for i in range(N):
    if data[i] == 0:
        data[i] = 2
        seat = i
        # print(seat)
        for j in idx:
            dis.append(abs(i-j))
# print(dis)  # [1, 1, 5, 3, 1, 3, 4, 2, 2, 5, 3, 1]
result = []
for i in range(0, len(dis), len(idx)):
    result.append(min(dis[i:i+len(idx)]))
print(max(result))