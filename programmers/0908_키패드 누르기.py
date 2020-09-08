def distance(ls1, ls2):
    dis = abs(ls1[0] - ls2[0]) + abs(ls1[1] - ls2[1])
    return dis


def solution(numbers, hand):
    board = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 0, 11]]

    ll = [(3, 0)]
    rr = [(3, 2)]

    answer = ''
    for number in numbers:
        for i in range(4):
            for j in range(3):
                if board[i][j] == number and board[i][j] in [1, 4, 7]:
                    ll.pop(0)
                    ll.append((i, j))
                    answer += 'L'

                elif board[i][j] == number and board[i][j] in [3, 6, 9]:
                    rr.pop(0)
                    rr.append((i, j))
                    answer += 'R'

                elif board[i][j] == number and board[i][j] in [2, 5, 8, 0]:
                    target = [i, j]
                    dis_left = distance(ll[0], target)
                    dis_right = distance(rr[0], target)
                    if dis_left > dis_right:
                        answer += 'R'
                        rr.pop(0)
                        rr.append([i, j])

                    elif dis_left < dis_right:
                        answer += 'L'
                        ll.pop(0)
                        ll.append([i, j])

                    else:
                        if hand == 'right':
                            answer += 'R'
                            rr.pop(0)
                            rr.append([i, j])
                        else:
                            answer += 'L'
                            ll.pop(0)
                            ll.append([i, j])

    return answer

# numbers = [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]
# hand = 'right'

# numbers = [7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2]
# hand = 'left'

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
hand = 'right'

