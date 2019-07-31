# X, Y = 3, 5
# A_list = [1, 5, 3]
# B_list = [3, 6, -7, 5, 4]

T = int(input())
for t in range(1, T + 1):
    X, Y = map(int, input().split())  # 3 5
    result = []
    if 3 <= (X and Y) <= 20:
        A_list = list(map(int, input().split()))  # A_list = [1, 5, 3]
        B_list = list(map(int, input().split()))  # B_list = [3, 6, -7, 5, 4]

        if X <= Y:
            for j in range(Y - X + 1): # 0, 1, 2
                total = 0
                for i in range(X):
                    total += (A_list[i] * B_list[i + j])
                result.append(total)

        if X > Y:
            for j in range(X - Y + 1): # 0, 1, 2
                total = 0
                for i in range(Y):
                    total += (B_list[i] * A_list[i + j])
                result.append(total)
        
        print(f'#{t} {max(result)}')
