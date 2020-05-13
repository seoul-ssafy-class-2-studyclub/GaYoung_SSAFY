def solution(progresses, speeds):
    ans = []

    # progresses에서 100이 넘으면 순서대로 뺄 것
    while progresses:
        for i in range(len(progresses)):
            progresses[i] += speeds[i]

        # 진행 상황이 100 이상이면, 배포 가능함
        # 이 때, 배포할 때 progresses, speeds 모두 제거
        # -> progresses가 존재할때 progresses[0] >= 100 인 경우에 p, s제거하고 cnt+=1
        cnt = 0
        while progresses and progresses[0] >= 100:
            progresses.pop(0)
            speeds.pop(0)
            cnt += 1
        # print(cnt)

        if cnt >= 1:
            ans.append(cnt)

    return ans
