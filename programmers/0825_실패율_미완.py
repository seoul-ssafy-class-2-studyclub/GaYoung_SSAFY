N = 5
stages = [2, 1, 2, 6, 2, 4, 3, 3]

# N = 4
# stages = [4, 4, 4, 4, 4]


for i in range(1, N+1):
    cnt = stages.count(i)

    if cnt