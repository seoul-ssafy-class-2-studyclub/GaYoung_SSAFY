def solution(board, moves):
    B = len(board)
    bd = [[0 for _ in range(B)] for _ in range(B)]
    for i in range(B):
        for j in range(B):
            bd[i][j] = board[j][i]

    result = [0]
    answer = 0
    for m in moves:
        # cnt = 0  # bd[m-1]이 다 0으로 되어있는지 확인하기 위해서
        for k in range(len(bd[m - 1])):
            if bd[m - 1][k] != 0:  # for k in bd[m-1]:해서 if k !=0 이라고하면 이따 k=0으로 하면 board에 안바뀜
                if result[-1] == bd[m - 1][k]:
                    result.pop()
                    answer += 2
                else:
                    result.append(bd[m - 1][k])
                bd[m - 1][k] = 0
                break

            # cnt += 1

            # if cnt == len(bd[m - 1]):
            #     break

    return answer

board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
moves = [1,5,3,5,1,2,1,4]

print(solution(board,moves))
'''
1. board가 가로로 맨 윗줄부터 나와있는것이기 때문에 세로로 돌린다 
 board = [[0,0,0,4,3],
          [0,0,2,2,5],
          [0,1,5,4,1],
          [0,0,0,4,3],
          [0,3,1,2,1]]
2. for i in moves: moves 돌면서 해당 board[i-1]중에 0이 아닌 첫번째값이 나오면 
   answer리스트에 추가하고 0으로 바꾼다
     - 이때, board판에 다 0이면 아무것도 일어나지 않음
'''
