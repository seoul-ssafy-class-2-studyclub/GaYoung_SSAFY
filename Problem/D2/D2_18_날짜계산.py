for t in range(int(input())):
    months = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    day_in_month = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
    f_month, f_day, s_month, s_day = map(int, input().split())
    day = 0

    if f_month +1 == s_month:
        day += s_day + day_in_month[f_month] - f_day + 1
    elif f_month +1 < s_month:
        choose_month = months[f_month : s_month - 1]
        for c_month in choose_month:
            day += day_in_month[c_month]
        day += day_in_month[f_month] - f_day + 1 + s_day
    else:
        day += s_day - f_day + 1

    print('#{0} {1}'.format(t+1, day))