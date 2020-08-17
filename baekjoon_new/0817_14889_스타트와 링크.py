'''
4
0 1 2 3
4 0 5 6
7 1 0 2
3 4 5 0

6
0 1 2 3 4 5
1 0 2 3 4 5
1 2 0 3 4 5
1 2 3 0 4 5
1 2 3 4 0 5
1 2 3 4 5 0

8
0 5 4 5 4 5 4 5
4 0 5 1 2 3 4 5
9 8 0 1 2 3 1 2
9 9 9 0 9 9 9 9
1 1 1 1 0 1 1 1
8 7 6 5 4 0 3 2
9 1 9 1 9 1 0 9
6 5 4 3 2 1 9 0
'''

from itertools import combinations

N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]

# combination 함수로 만들기
people = [i for i in range(N)]
start = list(combinations(people, N//2))  # // : 나눗셈 후 몫 반환, / : 7/4=1.25
all_people = set(people)

mymin = 9999999999999999999999999999999999
for star in start:
    link = list(all_people - set(star))

    link_sum = 0
    start_sum = 0
    # for a, b in star:  # 이렇게 되면 2명일때밖에 못한다.
    #     start_sum += board[a][b] + board[b][a]
    for i in range(N//2 - 1):
        for j in range(i+1, N//2):
            start_sum += board[star[i]][star[j]] + board[star[j]][star[i]]
            link_sum += board[link[i]][link[j]] + board[link[j]][link[i]]

            diff = abs(start_sum - link_sum)
            print('diff')
            print(diff)

    if mymin > diff:
        mymin = diff

print(mymin)

