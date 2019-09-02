N = int(input())
max_total = 0
data = []
for n in range(N):
    data.append(list(map(int, input().split())))

def max_work(k, total):
    global max_total
    if k >= N:
        if total > max_total:
            max_total = total
        return
    else:
        for i in range(2):
            if i == 0:  ## 안고르는 경우
                max_work(k+1, total)
            elif i == 1:
                if k + data[k][0] > N:
                    if total > max_total:
                        max_total = total
                    return
                max_work(k + data[k][0], total + data[k][1])

max_work(0, 0)
print(max_total)