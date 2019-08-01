for t in range(1):
    N = int(input())
    board =[]
    re_board = []
    n = 8

    for i in range(n):
        board.append(input())
        re_board = list(map(list, zip(*board)))
    print(board)  # ['CBCABBAC' 'BBABCABA', 'ABCBCCCA']
    print(re_board)  # [['C', 'B', 'A', 'B', 'B', 'C', 'C', 'C'],

    for k in range(n):  # 행
        for l in range(1, n+1):  #길이
            for j in range(n-l):  # 몇번째부터 검사하는지
                if board[k][j] != board[k][j-8+l]:
                    break
                else:
                    print('board[k][j]')


# <회문 구하는 방법>
# def isPalindrome(x):
#     result = True
#     for i in range(len(x) // 2):
#     if x[i] != word[-1-i]:
#         result = False
#         break
#     return result
