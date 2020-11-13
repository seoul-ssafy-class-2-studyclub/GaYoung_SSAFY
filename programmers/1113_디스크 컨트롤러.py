def solution(jobs):
    len_jobs = len(jobs)
    jobs = sorted(jobs, key=lambda x: x[1])
    start = 0
    answer = 0
    while jobs:

        for i in range(len(jobs)):
            # print(jobs)
            # print(i)
            if jobs[i][0] <= start:
                start += jobs[i][1]
                answer += start - jobs[i][0]
                jobs.pop(i)
                # print('start')
                # print(start)
                # print('answer')
                # print(answer)
                break

            if i == len(jobs) - 1:  # 작업이 들어오지 않으면
                start += 1
                # print('start')
                # print(start)

    # print('final answer')
    # print(answer)
    return answer // len_jobs

jobs = [[0, 3], [1, 9], [2, 6]]

