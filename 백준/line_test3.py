N = int(input())
time_s = []
time_e = []
for n in range(N):
    start, end = map(int, input().split())
    time_s.append(start)  # [[0, 10], [10, 15], [20, 30]]
    time_e.append(end)
print(time_s)  # [0, 10, 20, 25]
print(time_e)  # [10, 15, 30, 40]

toilet = 0
finish = []
for i in range(1, N):  # start
    if len(finish) == 0:
        finish.append(time_e[0])
    elif max(finish) < time_s[i]:
        toilet += 1
        finish.append(time_e[i])

print(toilet)
print(finish)





# print(toilet)