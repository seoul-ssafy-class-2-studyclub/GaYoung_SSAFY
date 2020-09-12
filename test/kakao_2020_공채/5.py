def solution(play_time, adv_time, logs):
    answer = ''
    return answer

# play_time = "02:03:55"
# adv_time = "00:14:15"
# logs = ["01:20:15-01:45:14", "00:40:31-01:00:00", "00:25:50-00:48:29", "01:30:59-01:53:29", "01:37:44-02:02:30"]
play_time = "01:10:55"
adv_time = "00:14:15"
logs = ["00:40:31-01:00:00", "00:25:50-00:48:29"]

def make_time(start_time, adv_time):
    hour = start_time[0] + adv_time[0]
    minute = start_time[1] + adv_time[1]
    if minute >= 60:
        hour += 1
        minute -= 60
    second = start_time[2] + adv_time[2]
    if second >= 60:
        minute += 1
        second -= 60
        if minute >= 60:
            hour += 1
            minute -= 60

    return [hour,minute,second]

log_data = []
end = []
for i in range(len(logs)):
    start, end = logs[i].split('-')
    hh1, mm1, ss1 = start.split(':')
    start = [int(hh1), int(mm1), int(ss1)]
    hh2, mm2, ss2 = end.split(':')
    end = [int(hh2), int(mm2), int(ss2)]
    log_data.append([start, end])

log_data = sorted(log_data, key=lambda x:(x[0][0], x[0][1], x[0][2]))

h1, m1, s1 = adv_time.split(':')
adv_time = [int(h1), int(m1), int(s1)]

h2, m2, s2 = play_time.split(':')
play_time = [int(h2), int(m2), int(s2)]
idx = 0
start_time = log_data[0][0]

if play_time == adv_time:
    print('00:00:00')

# for i in range(1, len(log_data)):
