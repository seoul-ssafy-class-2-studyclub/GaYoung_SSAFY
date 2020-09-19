# key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
# lock = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]

'''
[로직]
1. (key-1)*2+lock길이만큼의 board를 만든다.
2. key를 한칸씩 이동하면서 넣고, lock도 넣는다. 이때, board[i][j] != 1이면 멈춘다.
3. key 이동이 (0,0)부터 끝까지 갔으면, key를 90도 돌린다(함수만들기)
4. 열쇠로 자물쇠를 열수 있으면 true를, 열 수 없으면 false를 return
'''

def rotate(arr):
    n = len(arr)
    board = [[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            board[j][n-i-1] = arr[i][j]

    return board


def check(total, len_key, start_lock, end_lock, i, j, key, lock):
    board = [[0] * total for _ in range(total)]

    for key_i in range(len_key):
        for key_j in range(len_key):
            board[i + key_i][j + key_j] += key[key_i][key_j]

    for lock_i in range(start_lock, end_lock):
        for lock_j in range(start_lock, end_lock):
            board[lock_i][lock_j] += lock[lock_i - start_lock][lock_j - start_lock]

            if board[lock_i][lock_j] != 1:
                return False

    return True


def solution(key, lock):

    len_key = len(key)
    len_lock = len(lock)
    total = len_lock + 2 * (len_key - 1)
    start_lock = len_key-1
    end_lock = len_lock + len_key - 1

    for k in range(4):
        for i in range(end_lock):
            for j in range(end_lock):
                if check(total, len_key, start_lock, end_lock, i, j, key, lock):
                    return True

        key = rotate(key)

    return False

# print(solution(key, lock))
