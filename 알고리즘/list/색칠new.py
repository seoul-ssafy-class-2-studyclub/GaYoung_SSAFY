# def xy(r1, c1, r2, c2, color):
#     data = []
#     if color == 1:
#         for i in range(r1, r2+1):
#             for j in range(c1, c2+1):
#                 data.append((i, j))
#     elif color == 2:
#         for i in range(r1, r2+1):
#             for j in range(c1, c2+1):
#                 data.append((i, j))        
#     return data   # {(3, 2), (3, 3), (4, 4), (2, 3), (4, 3), (2, 2), (4, 2), (3, 4), (2, 4)}

# print(xy(2, 2, 4, 4, 1))
# print(xy(3, 3, 6, 6, 2))

# data1_set = {}
# data2_set = {}

# for t in range(int(input())):  # 3
#     N = int(input())  # 2
#     for i in range(N):
#         r1, c1, r2, c2, color = map(int, input().split())  # int, 2 2 4 4 1
#         data = xy(r1, c1, r2, c2, color)
#         if color == 1:
#             data1_set.update(data)
#         else:
#             data2_set.update(data)
#         print(data1_set)
#         # data1_set & data2_set)

#     # print('#{0} {1}'.format(t+1, len(both)))


# # data1 -> color = 1 일때
# # data2 -> color = 2 일때






board = [[0 for i in range(10)] for i in range(10)]

def is_color(r1, c1, r2, c2, color):
    # for r in range(r1, r2+1):
    #     for c in range(c1, c2+1):
            # if board[r][c] == 0:
            #     board[r][c] = color
            
            # elif board[r][c] != 3 and board[r][c] != color:
            #     board[r][c] = 3
            #     count += 1
    
    if color == 1:
        for r in range(r1, r2+1):
            for c in range(c1, c2+1):
                board[r][c] += 1
    if color == 2:
        for r in range(r1, r2+1):
            for c in range(c1, c2+1):
                board[r][c] += 2
    return board






for t in range(int(input())):
    board = [[0 for i in range(10)] for i in range(10)]  # 보드 초기화!!!
    N = int(input())
    count = 0
    for i in range(N):
        r1, c1, r2, c2, color = map(int, input().split())  # int, 2 2 4 4 1
        data = is_color(r1, c1, r2, c2, color)
    for r in range(10):
        for c in range(10):
            if data[r][c] >= 3:
                count += 1
    print('#{0} {1}'.format(t+1, count))
