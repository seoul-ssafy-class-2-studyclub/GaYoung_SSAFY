
# 1. 조합
#     1-1. 조합 하나가 구성되었을 때, 그에 따른 dis 구함
# 2. 백트레킹 mymin vs dis

def func(dis, cnt):
    global mymin

    if mymin < sum:  # 백트래킹
        return

    elif cnt == N:  # 만약 data갯수만큼 하나하나 1~4개까지 하고싶다면, for문 돌리기!
        # result.append(arr)
        # return result

    else:
        for idx in range(2, N + 2):
            if visit[idx] == False:
                visit[idx] = True
                x, y = dis[i]
                

            elif visit[idx] == False:
                visit[idx] = True
                perm(arr + [data[idx]])
                visit[idx] = False  # 전 단계의 visit만 초기화


for t in range(int(input())):
    N = int(input())
    word = list(map(int, input().split()))  # 값 그대로 받아오기
    data = [n for n in range(2, N+2)]  # 1~5의 조합 찾기
    visit = [False] * (N + 2)   # perm에 필요
    dis = []

    for i in range(0, (N+2)*2, 2):
        dis.append([word[i], word[i+1]])

    mymin = 9999999999999999999999999999999