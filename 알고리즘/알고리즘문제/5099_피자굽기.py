for t in range(int(input())):
    N, M = map(int, input().split())
    cheese = []
    data = list(map(int, input().split()))
    for m in range(M):
        cheese.append([m + 1, data[m]])

    queue = []
    for n in range(N):
        queue.append(cheese.pop(0))

    result = 0
    i = 0
    while queue:   # queue에 값이 들어있을때까지!!!!
        if queue[i][1] // 2 == 0:
            if len(cheese) == 0:
                a = queue.pop(0)
                # print(queue)
            elif len(cheese) > 0:
                queue.pop(0)
                queue.append(cheese.pop(0))
        elif queue[i][1] // 2 != 0:
            if len(queue) == 1:
                # print('break')
                a = queue.pop()
                break
            else:
                queue[i][1] = queue[i][1] // 2
                queue.append(queue.pop(0))
    # print(a)
    print('#{} {}'.format(t+1, a[0]))