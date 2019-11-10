a, b = map(int, input().split())
time = []
for i in range(a):
    time.append(int(input()))

total = [[] for _ in range(b)]
for i in range(b):
    total[i].append([0]*time[i])
# print(len(total[]))

for i in range(b):
    for j in range(b, len(time)):
        print(min(len(total[i])))

# print(c1)
# print(c2)