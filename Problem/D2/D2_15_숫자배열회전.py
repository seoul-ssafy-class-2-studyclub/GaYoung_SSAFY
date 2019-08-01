for t in range(int(input())):
    N = int(input())
    board = []
    result = ''
    a, b, c = [], [], []

    for i in range(N):  # 보드만들기
        board.append(list(input().split()))

    # 741 825 963 뽑기(밑에서 올라가기)
    for k in range(N):
        for j in range(N-1, -1, -1):
            result += board[j][k]
        a.append(result)
        result = ''

        
    # 987 654 321 뽑기 (오른쪽에서 왼쪽)
    for l in range(N-1, -1, -1):
        cross = reversed(board[l])
        b += [''.join(cross)]


    # 369 258 147 뽑기 (아래로 내려가기)
    for n in range(N-1, -1, -1):
        for m in range(N):
            result += board[m][n]
        c.append(result)
        result = ''
    
    print('#{0}'.format(t+1))
    answer = list(zip(a, b, c))
    for ans in answer:
        total = ' '.join(ans)
        print('{0}'.format(total))
