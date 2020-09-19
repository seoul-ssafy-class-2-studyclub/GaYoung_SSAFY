# n회 t분간격 최대m명
n, t, m, timetable = 1, 1, 5, ['08:00', '08:01', '08:02', '08:03'] # case 1
# n, t, m, timetable = 2, 10, 2, ['09:10', '09:09', '08:00'] # case 2
# n, t, m, timetable = 2, 1, 2, ['09:00', '09:00', '09:00', '09:00'] # case 3
# n, t, m, timetable = 1, 1, 5, ['00:01', '00:01', '00:01', '00:01', '00:01'] # case 4
# n, t, m, timetable = 1, 1, 1, ['23:59'] # case 5
# n, t, m, timetable = 10, 60, 45, ['23:59', '23:59', '23:59', '23:59', '23:59', '23:59', '23:59', '23:59', '23:59', '23:59', '23:59', '23:59', '23:59', '23:59', '23:59', '23:59'] # case 6


def change(time):  # 분으로 통일
    time = list(map(int,time.split(':')))
    hour = int(time[0]) * 60
    minute = int(time[1])
    return hour + minute

def make_time(number):
    hour = number // 60
    minute = number % 60
    hour, minute = str(hour), str(minute)

    for i in range(2-len(hour)):
        hour = '0' + hour

    for i in range(2 - len(minute)):
        minute = '0' + minute

    return hour + ':' + minute


def solution(n, t, m, timetable):
    timetable = list(map(change,timetable))
    timetable.sort(reverse=True)

    start = 9 * 60  # 9시
    for _ in range(n):
        bus = []
        for _ in range(m):
            if timetable:
                if timetable[-1] <= start:
                    bus.append(timetable.pop())

        start += t  # 다음 셔틀

    # 마지막 셔틀에서 +t가 되기 때문에 start -= t를 해줘야한다.
    start -= t
    if len(bus) == m:
        print(bus[-1])
        return make_time(bus[-1] - 1)  # m = 2, bus = ['09:09', '09:10']이면 9:10보다 1분 빠르면 됨

    else:
        return make_time(start)  # m = 2, bus = ['09:09']이면 셔틀 출발시간에 도착해도 괜찮다.

print(solution(n, t, m, timetable))