def solution(dartResult):
    dart = dartResult.replace('10', 't')
    # print(dart)

    bonus = {'S': 1, 'D': 2, 'T': 3}
    option = ['*', '#']
    ans = []
    for i in range(len(dart)):
        if dart[i] in bonus:
            if dart[i - 1] == 't':
                ans.append(10 ** bonus[dart[i]])
            else:
                ans.append(int(dart[i - 1]) ** bonus[dart[i]])
        elif dart[i] in option:
            if dart[i] == '*':
                if len(ans) == 1:
                    ans[-1] = 2 * ans[-1]
                else:
                    ans[-2], ans[-1] = 2 * ans[-2], 2 * ans[-1]
            else:
                ans[-1] = -ans[-1]

    return sum(ans)


dartResult = '1S2D*3T'
