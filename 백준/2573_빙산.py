N, M = map(int, input().split())
ice = []

for n in range(N):
    ice.append(list(map(int, input().split())))

queue = []
near = [(-1, 0), (0, 1), (1, 0), (0, -1)]


for i in range(N):
    for j in range(M):
        if ice[i][j] != 0:
            queue.append(i)
            queue.append(j)
            cnt = 0
            while queue:
                x = queue.pop(0)
                y = queue.pop(0)
                for a, b in near:
                    xi = x + a
                    yi = y + b
                    if 0 <= xi < N and 0 <= yi < N:
                        if ice[xi][yi] == 0:
                            cnt += 1
            ice[i][j] = ice[i][j] - cnt

# ice[i][j] - cnt
print(ice)