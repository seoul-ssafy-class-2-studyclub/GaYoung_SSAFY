from collections import deque

def solution(n, delivery):
    delivery = sorted(delivery, key=lambda x: (-x[2], x[0], x[1]))
    delivery = deque(delivery)

    check = ['0'] * n  # 'O'=1, 'X'=2, '?'=3
    circle = []
    restart = deque([])
    while delivery:
        first, second, go = delivery.popleft()
        if go == 1:
            check[first - 1] = 'O'
            check[second - 1] = 'O'
            circle.append(first)
            circle.append(second)

        # [1, 5, 0], [2, 5, 0], [5, 6, 0], [7, 6, 0]])
        elif go == 0 and (first in circle or second in circle):
            if check[first - 1] == 'O' and check[second - 1] == '0':
                check[second - 1] = 'X'
            elif check[second - 1] == 'O' and check[first - 1] == '0':
                check[first - 1] = 'X'
        elif go == 0 and first not in circle and second not in circle:
            restart.append([first, second, go])

    while restart:
        first, second, go = restart.popleft()
        if check[second - 1] == 'X' and check[first - 1] == '0':
            check[first - 1] = '?'
        elif check[first - 1] == 'X' and check[second - 1] == '0':
            check[second - 1] = '?'
        elif check[first - 1] == '?' and check[first - 1] == '0':
            check[second - 1] = '?'
        elif check[second - 1] == '?' and check[second - 1] == '0':
            check[first - 1] = '?'

    # print(check)
    answer = ''.join(check)
    answer = answer.replace('0', '?')
    # print(answer)

    return answer

# n = 6
# delivery = [[1,3,1],[3,5,0],[5,4,0],[2,5,0]]


n = 7
delivery = [[5,6,0],[1,3,1],[1,5,0],[7,6,0],[3,7,1],[2,5,0]]

# n = 6
# delivery = [[1, 3, 1], [2, 4, 0], [2, 5, 0]]

print(solution(n, delivery))

'''

            elif check[second - 1] == 'X' and check[first - 1] == '0':
                check[first - 1] = '?'
            elif check[first - 1] == 'X' and check[second - 1] == '0':
                check[second - 1] = '?'
            elif check[first - 1] == '?' and check[first - 1] == '0':
                check[second - 1] = '?'
            elif check[second - 1] == '?' and check[second - 1] == '0':
                check[first - 1] = '?'
'''