import pprint

# key = [[0, 0, 1], [0, 0, 1], [0, 1, 0]]
# key = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
key = [[0, 1, 0], [1, 0, 0], [1, 0, 0]]
# key = [[1, 1, 0], [0, 0, 1], [0, 0, 0]]
lock = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]

'''
key를 가지고 lock[i][j] == 0 인 곳에 가서 확인하고 key 90도 돌리면서 확인하기
load를 key도 갈수있게 확장하기
'''


def rotate(arr):
    n = len(arr)
    board = [[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            board[j][n-i-1] = arr[i][j]

    return board


def check(i, j, total, lock_start, lock_end, key, lock):
    board = [[0] * total for _ in range(total)]

    for key_i in range(len(key)):
        for key_j in range(len(key)):
            board[i + key_i][j + key_j] += key[key_i][key_j]

    for lock_i in range(lock_start, lock_end):
        for lock_j in range(lock_start, lock_end):
            board[lock_i][lock_j] += lock[lock_i - lock_start][lock_j - lock_start]

            if board[lock_i][lock_j] != 1:
                return False

    return True


def solution(key, lock):
    key_length = len(key)
    lock_length = len(lock)
    total = lock_length + 2 * (key_length - 1)
    lock_start = key_length - 1
    lock_end = lock_length + key_length - 1

    for k in range(0, 4):
        for i in range(lock_end):
            for j in range(lock_end):
                result = check(i, j, total, lock_start, lock_end, key, lock)
                if result:
                    return True

        key = rotate(key)
    return False

print(solution(key, lock))

