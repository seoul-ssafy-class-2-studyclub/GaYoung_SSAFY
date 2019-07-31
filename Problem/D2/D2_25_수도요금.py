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


# gayoung
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


# another 1
for T in range(int(input())):
    P, Q, R, S, W = map(int, input().split())
    r = 0
    A = W*P
    if W < R:
        B = Q
    elif W > R:
        B = Q + ((W-R)*S)
    if A >= B:
        r = B
    elif A <= B:
        r = A
    print(f'#{T+1} {r}')


# another 2
T = int(input())

for i in range(T):
    
    p, q, r, s, w = list(map(int,input().split())) #각각의 변수에 값을 입력
    
    a = w * p 										#A사 요금
    b = q if w <= r else q + (w - r) * s	  #B사 요금

    price = min(a, b) 								#둘중 낮은가격

    print(f'#{i+1} {price}')
