# 스타트 팀, 링크 팀의 능력치 차이 최소화
'''
4
0 1 2 3
4 0 5 6
7 1 0 2
3 4 5 0
'''
from itertools import combinations

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
people = [i for i in range(N)]

start = list(combinations(people, N // 2))
all = set(people)

res = 9999999999999999999999999999999999
for s in start:
    link = list(all - set(s))

    cnt_start = 0
    cnt_link = 0
    n = N // 2

    for i in range(n - 1):
        for j in range(i + 1, n):
            cnt_start += board[s[i]][s[j]] + board[s[j]][s[i]]
            cnt_link += board[link[i]][link[j]] + board[link[j]][link[i]]
            diff = abs(cnt_link - cnt_start)

            if res > diff:
                res = diff
print(res)