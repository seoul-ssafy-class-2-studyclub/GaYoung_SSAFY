def solution(progresses, speeds):
    answer = []

    while progresses:
        for i in range(len(progresses)):
            progresses[i] += speeds[i]
        # print(progresses)

        cnt = 0
        while progresses and progresses[0] >= 100:
            progresses.pop(0)
            speeds.pop(0)
            cnt += 1

        if cnt >= 1:
            answer.append(cnt)

    # print(answer)
    return answer

progresses = [93,30,55]
speeds = [1,30,5]
