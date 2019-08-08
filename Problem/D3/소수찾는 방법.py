def min_insu(num):
    for i in range(2, num // 2):
        if not num % i:
            return i
​
              
numbers = [26, 39, 51, 53, 57, 79, 85]
​
board = [False, False, True]+[True]*(max(numbers) - 2)
​
for i in range(2, len(board)):
    if board[i]:
        for l in range(2 * i, len(board), i):
            board[l] = False
​
​
# 아래에 코드를 작성하세요
for number in numbers:
    if board[number]:
        print(f'{number} 는 소수입니다.')
    else:
        print(f'{number} 는 소수가 아닙니다. {min_insu(number)} 는 {number} 의 인수입니다.')