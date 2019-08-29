data = []
for n in range(9):
    data.append(int(input()))
# print(data)  # [20, 7, 23, 19, 10, 15, 25, 8, 13]

total_nine = sum(data)
two = []
flag = 0
for i in range(8):
    for j in range(i + 1, 9):
        total = total_nine - data[i] - data[j]
        if total == 100:
            data.pop(j)
            data.pop(i)
            flag = 1
            break
    if flag:
        break

for d in sorted(data):
    print(d)