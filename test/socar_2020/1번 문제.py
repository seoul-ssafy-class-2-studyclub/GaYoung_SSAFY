bakery_schedule = ['09:05 10', '12:20 5','13:25 6','14:24 5']
current_time = '12:05'
K = 10

# bakery_schedule = ['12:00 10']
# current_time = '12:00'
# K = 11

# bakery_schedule = ['12:00 10']
# current_time = '12:00'
# K = 10

def time_check(current_time, bread_time):
    answer = 0
    c1, b1 = int(current_time[:2]), int(bread_time[:2])
    c2, b2 = int(current_time[3:]), int(bread_time[3:])

    if b1 > c1 and b2 > c2:
        answer += (b1-c1) * 60 + (b2-c2)
    elif b1 > c1 and b2 < c2:
        answer += (b1-c1) * 60 - (c2-b2)
    elif b1 == c1 and b2 > c2:
        answer += (b2-c2)
    elif b2 == c2 and b1 > c1:
        answer += (b1-c1) * 60

    return answer


ans = 0
cnt = 0  # K와 비교

check_time = current_time
for bakery in bakery_schedule:
    time, bread = bakery.split()
    h1, h2 = int(time[:2]), int(current_time[:2])
    m1, m2 = int(time[3:]), int(current_time[3:])
    if h1 >= h2:
        if m1 >= m2:
            cnt += int(bread)
            ans += time_check(check_time, time)
            check_time = time

    if K <= cnt:
        print(ans)
        break

if K > cnt:
    print(-1)

