key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
lock = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]

def rotate(key):
    l_key = len(key)
    bd = [[0] * l_key for _ in range(l_key)]
    for i in range(l_key):
        for j in range(l_key):
            bd[j][l_key-i-1] = key[i][j]
    return bd

def check(total_len, len_key, start_lock, i, j, end_lock, key, lock):
    board = [[0] * total_len for _ in range(total_len)]
    for x in range(len_key):
        for y in range(len_key):
            board[i + x][j + y] += key[x][y]

    for x in range(start_lock, end_lock):
        for y in range(start_lock, end_lock):
            board[x][y] += lock[x - start_lock][y - start_lock]

            if board[x][y] != 1:
                return False

    return True

def solution(key, lock):
    len_key = len(key)
    len_lock = len(lock)
    total_len = (len(key) - 1) * 2 + len_lock

    start_lock = len_key - 1
    end_lock = len_lock + len_key - 1

    for k in range(4):
        for i in range(end_lock):
            for j in range(end_lock):
                if check(total_len, len_key, start_lock, i, j, end_lock, key, lock):  # key를 들고다녀야 바뀐 key값이 적용된다.
                    return True

        key = rotate(key)

    return False

print(solution(key, lock))

