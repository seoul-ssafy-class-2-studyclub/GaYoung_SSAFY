# T = int(input())

# for t in range(1, T + 1):

# 퍼즐 보드 만들기
n, k = list(map(int, input().split()))  # 5(=n) 3(=k) 
board = []
for i in range(n):
    board.append(list(input().split())) # board라는 list에 넣기
print(board)


# 가로로 연속 3개
# for문 돌려서  0 0 1 1 1 뽑아내고 거기서 연속으로 3개인 것 갯수찾기
row_result = 0
row_count = 0  # 3개가 되면 result에 1씩 추가
for j in range(n):
    print(board[j])

    3개를 [0] = [1] 비교