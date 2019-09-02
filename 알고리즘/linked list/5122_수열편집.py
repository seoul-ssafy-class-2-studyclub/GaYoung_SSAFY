for t in range(int(input())):
    N, M, L = map(int, input().split())
    data = list(map(int, input().split()))
    for m in range(M):
        move = input().split()
        if move[0] == 'I':
            idx = int(move[1])
            num = int(move[2])
            data[idx:0] = [num]
        elif move[0] == 'D':
            idx = int(move[1])
            data.pop(idx)
        elif move[0] == 'C':
            idx = int(move[1])
            num = int(move[2])
            data[idx] = num
    if L + 1 > len(data):
        result = -1
    else:
        result = data[L]
    print('#{} {}'.format(t+1, result))