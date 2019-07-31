# 85 72 38 80 69 65 68 96 22
num = list(map(int, input().split()))  # [85 72 38 80 69 65 68 96 22]
num.sort()  # [22, 38, 65, 68, 69, 72, 80, 85, 96]

i = (len(num) - 1) // 2
print(i)  # 4

print(num[i])