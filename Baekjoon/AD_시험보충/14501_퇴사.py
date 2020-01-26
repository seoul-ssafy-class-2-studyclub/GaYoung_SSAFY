def work(i, total):
    global mymax
    if i >= N:
        if mymax < total:
            mymax = total
            return mymax
    else:
        # 채택 or 버림을 임의로 가정
        for k in range(2):
            if k == 0:  # 채택
                if i + data[i][0] <= N:
                    work(i + data[i][0], total + data[i][1])
            elif k == 1:  # 버림
                # 버리면 바로 다음거로 넘어감
                work(i + 1, total)

N = int(input())

data = []
for n in range(N):
    data.append(list(map(int, input().split())))

mymax = 0
work(0, 0)
print(mymax)