progresses = [95, 90, 99, 99, 80, 99]
speeds = [1, 1, 1, 1, 1, 1]
def solution(progresses, speeds):
    # 끝나는 요일 계산하기
    check = []

    for i in range(len(progresses)):
        x, y = divmod((100 - progresses[i]), speeds[i])

        if y == 0:
            check.append(x)
        elif y != 0:
            check.append(x + 1)

    # 몇일 째 몇개의 기능이 배포되는지 확인
    now = check[0]
    cnt = 0
    answer = []
    while check:
        x = check.pop(0)

        if x <= now:
            cnt += 1

        else:
            answer.append(cnt)
            cnt = 1
            now = x

    answer.append(cnt)  # 마지막으로 최대값이 나온 다음에 더해지는 cnt는 answer에 포함되지 않기때문에
                        # while문이 끝났을 때의 cnt를 넣어준다.
    # print(answer)

    return answer

print(solution(progresses,speeds))