# lines = ['2016-09-15 01:00:04.001 2.0s', '2016-09-15 01:00:07.000 2s']
# lines = ['2016-09-15 01:00:04.002 2.0s', '2016-09-15 01:00:07.000 2s']
lines = ['2016-09-15 20:59:57.421 0.351s', '2016-09-15 20:59:58.233 1.181s',
         '2016-09-15 20:59:58.299 0.8s', '2016-09-15 20:59:58.688 1.041s',
         '2016-09-15 20:59:59.591 1.412s', '2016-09-15 21:00:00.464 1.466s',
         '2016-09-15 21:00:00.741 1.581s', '2016-09-15 21:00:00.748 2.31s',
         '2016-09-15 21:00:00.966 0.381s', '2016-09-15 21:00:02.066 2.62s']

def solution(lines):
    time = []
    for line in lines:
        line = line.split(' ')
        end = list(map(int, line[1].replace('.', ':').split(':')))

        idx = 0
        for i in range(len(line[2])):
            if line[2][i] == 's':
                idx = i
        temp = float(line[2][:idx])

        end = end[3] + 1000 * end[2] + 1000 * 60 * end[1] + 1000 * 60 * 60 * end[0]  # 초로 바꾸기
        start = end - int(temp * 1000) + 1

        time.append([start, end])

    answer = 0
    for i in range(len(time)):
        cnt = 1
        for j in range(i + 1, len(time)):
            if time[j][1] - time[i][1] > 4000:  # 3초대 까지는 괜찮
                break
            if time[j][0] - time[i][1] < 1000:
                cnt += 1

        if answer < cnt:
            answer = cnt
    # print(answer)
    return answer