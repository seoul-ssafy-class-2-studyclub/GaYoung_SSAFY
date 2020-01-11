'''
7
3 6
7 3
4 2
1 4
5 7
2 5
6 1
'''
for t in range(int(input())):
    N = int(input())
    visit = [0] * (N + 1)
    score = [list(map(int, input().split())) for _ in range(N)]
    score.sort(reverse=True)

    for n in range(N, 0, -1):
        if visit[n] != 0:
            continue

        for m in range(n-1, 0, -1):

            if score[n][1] > score[m-1][1]:
                visit[m] += 1

    print(visit)
    cnt = 0
    for v in visit:
        if v == 0:
            cnt += 1
    print(cnt)
    print('========================================================')

'''
[0, 0, 0, 0, 0, 4]
4
-----------------------------------------

[0, 0, 1, 1, 0, 2, 0, 2]
3
-----------------------------------------
'''
'''
0, 0, 1, 1, 1, 1]
2
========================================================

[0, 0, 1, 0, 2, 1, 2, 3]
3
========================================================
'''