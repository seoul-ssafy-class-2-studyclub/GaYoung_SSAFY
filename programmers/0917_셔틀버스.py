def solution(n, t, m, timetable):
    answer = ''
    return answer


# n회 t분간격 최대m명
# n, t, m, timetable = 1, 1, 5, ['08:00', '08:01', '08:02', '08:03']
n, t, m, timetable = 2, 10, 2, ['09:10', '09:09', '08:00']
# n, t, m, timetable = 2, 1, 2, ['09:00', '09:00', '09:00', '09:00']
# n, t, m, timetable = 1, 1, 5, ['00:01', '00:01', '00:01', '00:01', '00:01']
# n, t, m, timetable = 1, 1, 1, ['23:59']
# n, t, m, timetable = 10, 60, 45, ['23:59', '23:59', '23:59', '23:59', '23:59', '23:59', '23:59', '23:59', '23:59', '23:59', '23:59', '23:59', '23:59', '23:59', '23:59', '23:59']


def shuttle_time(n, t):
    shuttle = ['09:00']
    hour = 9
    minute = 0
    for i in range(n-1):
        minute += t
        if minute >= 60:
            hour += 1
            minute = 0

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


timetable = sorted(timetable)
shuttle = shuttle_time(n, t)
shuttle_visit = [0] * len(shuttle)

for i in range(n):
    # cnt = 0

    if len(timetable) < m:  # case1
        print('shuttle[-1]')
        print(shuttle[-1])
        break

    for j in range(m-1, -1, -1):
        if timetable[j] <= shuttle[i]:
            timetable.pop(j)
        print('timetable')
        print(timetable)
        print('shuttle')
        print(shuttle[i])

    if i == n - 1:
        if timetable[0] > shuttle[i]:  # 문자열 비교 시 if '09:10' < '09:00': 계산 가능!!
            print(shuttle)


            if cnt < m:
                continue
            elif cnt == m-1:
