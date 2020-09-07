n, t, m = 1, 1, 5  # n회 t분간격 최대m명
timetable = ['08:00', '08:01', '08:02', '08:03']

# n, t, m = 2, 10, 2  # n회 t분간격 최대m명
# timetable = ['09:10', '09:09', '08:00']
#
# n, t, m = 2, 1, 2  # n회 t분간격 최대m명
# timetable = ['09:00', '09:00', '09:00', '09:00']
#
# n, t, m = 1, 1, 5  # n회 t분간격 최대m명
# timetable = ['00:01', '00:01', '00:01', '00:01', '00:01']
#
# n, t, m = 1, 1, 1  # n회 t분간격 최대m명
# timetable = ['23:59']

# n, t, m = 10, 60, 45  # n회 t분간격 최대m명
# timetable = ['23:59', '23:59', '23:59', '23:59', '23:59', '23:59', '23:59', '23:59', '23:59', '23:59', '23:59', '23:59', '23:59', '23:59', '23:59', '23:59']
# #

# n, t, m = 2, 10, 2  # n회 t분간격 최대m명
# timetable = ['09:10', '09:09', '08:00']

def shuttle(n, t):
    shuttle_time = [(9, 0)]
    hour = 9
    minute = 0
    for i in range(n-1):
        minute += t
        if minute >= 60:
            hour += 1
            minute = 0
        shuttle_time.append([hour, minute])

    return shuttle_time


def make_time(time):
    hour, minute = time[0], time[1]

    if hour < 10:
        hour = '0' + str(hour)
    else:
        hour = str(hour)

    if minute < 10:
        minute = '0' + str(minute)
    else:
        minute = str(minute)

    return hour + ':' + minute



def solution(n, t, m, timetable):
    shuttle_time = shuttle(n, t)
    print(shuttle_time)
    crew = []  # [[8, 0], [8, 1], [8, 2], [8, 3]]
    for time in timetable:
        hour, minute = time.split(':')
        crew.append([int(hour), int(minute)])

    crew.sort()
    print(crew)

    for i in range(n):
        cnt = 0
        if len(crew) < m:
            return make_time(shuttle_time[-1])

        # else:

    return 0

print(solution(n, t, m, timetable))