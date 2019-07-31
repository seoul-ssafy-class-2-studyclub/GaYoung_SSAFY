A = list(map(int, input().split()))  # [1, 5, 3]
B = list(map(int, input().split()))  # [3, 6, -7, 5, 4]

result = []
for j in range(len(B) + len(A) - 1):  # 0, 1, 2
    for i in range(len(A)):  # 0, 1, 2
        result = A[i+j] * B[j]
    
    print(result)
