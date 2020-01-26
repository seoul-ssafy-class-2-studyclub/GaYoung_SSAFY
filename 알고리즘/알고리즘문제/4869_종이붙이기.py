def paper(N):
    if N == 10:
        return 1
    if (N // 10) % 2 == 1:  # 홀수
        return paper(N - 10) * 2 - 1
    else:
        return paper(N - 10) * 2 + 1

for t in range(int(input())):
    N = int(input())
    print('#{} {}'.format(t+1, paper(N)))
