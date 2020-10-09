# n = 3
# customer = ["10/01 23:20:25 30", "10/01 23:25:50 26", "10/01 23:31:00 05", "10/01 23:33:17 24", "10/01 23:50:25 13", "10/01 23:55:45 20", "10/01 23:59:39 03", "10/02 00:10:00 10"]

n = 2
customer = ["02/28 23:59:00 03","03/01 00:00:00 02", "03/01 00:05:00 01"]

def check_time(month, day, h, m, s, long):
    if m + long >= 60:
        h += 1
        m = m + long - 60

    elif m + long < 60:
        m += long

    if h >= 24:
        day += 1
        h -= 24

    if month in [1, 3, 5, 7, 8, 10] and day == 32:
        month += 1
        day -= 30

    elif month in [4, 6, 9, 11] and day == 31:
        month += 1
        day -= 29

    elif month == 12 and day == 32:
        month = 1
        day = 1

    elif month == 2 and day == 29:
        month = 3
        day = 1

    answer = ''
    if 1 <= month < 10:
        month = '0' + str(month)
    elif month >= 10:
        month = str(month)
    if 0 <= day < 10:
        day = '0' + str(day)
    elif month >= 10:
        day = str(day)
    if 0 <= h < 10:
        h = '0' + str(h)
    elif h >= 10:
        h = str(h)
    if 0 <= m < 10:
        m = '0' + str(m)
    elif m >= 10:
        m = str(m)
    if 0 <= s < 10:
        s = '0' + str(s)
    elif s >= 10:
        s = str(s)
    answer += month + day + h + m + s
    return answer

machine = ['0' for _ in range(n)]

cnt = [0] * n
for i in range(len(customer)):
    date, time, long = customer[i].split()
    monthi, dayi = int(date[:2]), int(date[3:])
    hh, mm, ss = time.split(':')
    hhi, mmi, ssi = int(hh), int(mm), int(ss)
    longi = int(long)


    temp = check_time(monthi, dayi, hhi, mmi, ssi, longi)
    if i < n:
        if machine[i] == '0':
            machine[i] = temp
            cnt[i] += 1

    elif i >= n:
        mymin = min(machine)
        for x in range(n):
            if machine[x] == mymin:
                machine[x] = temp
                cnt[x] += 1
                break

    print(machine)
    print(cnt)