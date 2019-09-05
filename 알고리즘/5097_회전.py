for t in range(int(input())):
    N, M = map(int, input().split())
    data = list(map(int, input().split()))
    queue = [data.pop(0)]
    for m in range(M):
        data.append(queue.pop(0))
        queue.append(data.pop(0))
    result = queue.pop()
    print('#{} {}'.format(t+1, result))