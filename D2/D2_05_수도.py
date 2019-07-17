# T =int(input())

# for t in range(1, T + 1):
#     p, q, r, s, w = map(int, input().split())
#     A_com = w * p  # A회사 가격(언제나 동일)
#     B_com = q
#     if A_com < B_com:
#         print(f'#{t} {A_com}')
#     if B_com <= A_com:
#         if w < r:
#             print(f'#{t} {B_com}')
#         elif w >= r:
#             B_com += (w - r) * s
#             print(f'#{t} {B_com}')


# 어제밤
T =int(input())

for t in range(1, T + 1):
    p, q, r, s, w = map(int, input().split())
    A_com = w * p  # A회사 가격(언제나 동일)
    B_com = q
    if w > r:
        B_com += (w - r) * s
    if A_com <= B_com:
        print(f'#{t} {A_com}')
    else:
        print(f'#{t} {B_com}')