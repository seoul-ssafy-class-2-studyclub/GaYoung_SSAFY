def solution(numbers, hand):
    answer = ''
    board = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 0, 11]]

    ll = [(3, 0)]
    rr = [(3, 2)]

    for n in numbers:
        for i in range(4):
            for j in range(3):
                if board[i][j] == n == 1 or board[i][j] == n == 4 or board[i][j] == n == 7:
                    ll.pop(0)
                    ll.append((i, j))
                    answer += 'L'
                elif board[i][j] == n == 3 or board[i][j] == n == 6 or board[i][j] == n == 9:
                    rr.pop(0)
                    rr.append((i, j))
                    answer += 'R'
                elif board[i][j] == n == 2 or board[i][j] == n == 5 or board[i][j] == n == 8 or board[i][j] == n == 0:
                    l_c = abs(ll[-1][0] - i) + abs(ll[-1][1] - j)
                    r_c = abs(rr[-1][0] - i) + abs(rr[-1][1] - j)
                    # print('l_c')
                    # print(l_c)
                    # print('r_c')
                    # print(r_c)
                    # break
                    if l_c < r_c:
                        ll.append(board[i][j])
                        ll.pop()
                        ll.append((i, j))
                        answer += 'L'
                    elif l_c > r_c:
                        rr.append(board[i][j])
                        rr.pop()
                        rr.append((i, j))
                        answer += 'R'
                    else:
                        if hand == 'right':
                            rr.append(board[i][j])
                            rr.pop()
                            rr.append((i, j))
                            answer += 'R'
                        else:
                            ll.append(board[i][j])
                            ll.pop()
                            ll.append((i, j))
                            answer += 'L'

    return answer

    # print('answer')
    # print(answer)
    #
    # print('n')
    # print(n)
    # print('-----------------------------------------')