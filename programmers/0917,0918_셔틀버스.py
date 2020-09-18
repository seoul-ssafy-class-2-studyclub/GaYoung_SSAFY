# n회 t분간격 최대m명
# n, t, m, timetable = 1, 1, 5, ['08:00', '08:01', '08:02', '08:03'] # case 1
n, t, m, timetable = 2, 10, 2, ['09:10', '09:09', '08:00'] # case 2
# n, t, m, timetable = 2, 1, 2, ['09:00', '09:00', '09:00', '09:00'] # case 3
# n, t, m, timetable = 1, 1, 5, ['00:01', '00:01', '00:01', '00:01', '00:01'] # case 4
# n, t, m, timetable = 1, 1, 1, ['23:59'] # case 5
# n, t, m, timetable = 10, 60, 45, ['23:59', '23:59', '23:59', '23:59', '23:59', '23:59', '23:59', '23:59', '23:59', '23:59', '23:59', '23:59', '23:59', '23:59', '23:59', '23:59'] # case 6


def shuttle_time(n, t):
    shuttle = ['09:00']
    hour = 9
    minute = 0
    for i in range(n-1):
        minute += t
        if minute >= 60:
            hour += 1
            minute -= 60

        if hour == 9:
            if minute < 10:
                temp = '09:0' + str(minute)
                shuttle.append(temp)
            else:
                temp = '09:' + str(minute)
                shuttle.append(temp)

        else:
            if minute < 10:
                temp = str(hour) + ':0' + str(minute)
                shuttle.append(temp)
            else:
                temp = str(hour) + ':' + str(minute)
                shuttle.append(temp)

    return shuttle


def make_time(h, m):

    if int(m) == 0:
        if int(h) <= 10:
            answer = '0' + str(int(h) - 1) + ':59'
        else:
            answer = str(int(h) - 1) + ':59'
    elif int(m) <= 10:
        answer = h + ':0' + str(int(m) - 1)

    else:
        answer = h + ':' + str(int(m) - 1)

    return answer


def solution(n, t, m, timetable):
    timetable = sorted(timetable)
    shuttle = shuttle_time(n, t)

    for i in range(n):

        if len(timetable) < m:  # case 1
            return shuttle[-1]

        # 마지막 버스의 마지막 손님보다 1분 빠르거나 버스의 자리가 있으면 그냥 타는 것
        if i == n - 1:
            # case 5
            if timetable[0] > shuttle[i]:  # 문자열 비교 시 if '09:10' < '09:00': 계산 가능!!
                return shuttle[i]

            check = 0
            cnt = 0
            same = 0

            for k in range(len(timetable)):
                if timetable[k] < shuttle[i]:
                    cnt += 1
                    check = k

                    if cnt > m:
                        break

                if timetable[k] == shuttle[i]:
                    same += 1

            if same == 0 and cnt < m:
                return shuttle[i]

            elif same == 0 and cnt >= m:  # case 3
                hour, minute = timetable[check][:2], timetable[check][3:]
                return make_time(hour, minute)

            elif same != 0 and cnt + same == m:  # case 2  and cnt + same >= m
                # 이런 경우는 shuttle[i]보다 1분 빠르게 도착하면 됨.
                hour, minute = shuttle[i][:2], shuttle[i][3:]
                return make_time(hour, minute)

            elif same != 0 and cnt + same > m:  # case 2  and cnt + same >= m
                # 이런 경우는 shuttle[i]보다 1분 빠르게 도착하면 됨.
                hour, minute = timetable[check][:2], timetable[check][3:]

                return make_time(hour, minute)

            elif same != 0 and cnt + same < m:
                return shuttle[i]


        for j in range(m - 1, -1, -1):  # pop하기 때문에 마지막에 해줘야함
            if timetable[j] <= shuttle[i]:
                timetable.pop(j)


print(solution(n, t, m, timetable))