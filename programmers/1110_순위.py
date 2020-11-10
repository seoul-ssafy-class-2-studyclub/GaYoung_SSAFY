def solution(n, results):
    win = {}
    lose = {}

    for i in range(1, n + 1):
        win[i], lose[i] = set(), set()

    for i in range(1, n + 1):
        for winner, loser in results:
            if winner == i:
                win[i].add(loser)

            if loser == i:
                lose[i].add(winner)

        '''
        1은 2 이김
        2는 5 이김 -> 결론 : 1은 2, 5 이김 
        '''
        for winner in lose[i]:
            win[winner].update(win[i])

        for loser in win[i]:
            lose[loser].update(lose[i])

    # print(win)
    # print(lose)

    cnt = 0
    for i in range(1, n + 1):
        if len(win[i]) + len(lose[i]) == n - 1:
            cnt += 1

    # print(cnt)
    return cnt

n = 5
results = [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]
