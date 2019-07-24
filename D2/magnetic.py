# T = int(input())    # 1
# for t in range(1, T + 1):
size = int(input())
board = []   # 보드만들기
ans = []

for i in range(size):
    board.append(input().split()) # 보드바꾸기? -> 실패 -> N  [0][1][2]..[size]  S 
zip_board = list(map(list, zip(*board)))
# print(zip_board)  # 1 0 0 0 0 0 0으로 나온다

# 7
# 1 0 2 0 1 0 1
# 0 2 0 0 0 0 0
# 0 0 1 0 0 1 0
# 0 0 0 0 1 2 2
# 0 0 0 0 0 1 0
# 0 0 2 1 0 2 1
# 0 0 1 2 2 0 2


for j in range(size):  # 0~ 6까지 돌아간다.
    result = []
    for k in range(size):
        if zip_board[j][k] != '0':
            result.append(zip_board[j][k])
    # print(result)

# ['1']
# ['2']
# ['2', '1', '2', '1']
# ['1', '2']
# ['1', '1', '2']
# ['1', '2', '1', '2']
# ['1', '2', '1', '2']


    count = 0
    ans += [result]
# print(ans)
# print(type(ans[2][1]))

for a in ans:
    if a[0] == '2':
        a.pop(0)
print(ans)
    # if ans[a][-1] == '1':
    #     ans.pop(0)
    # print(ans)