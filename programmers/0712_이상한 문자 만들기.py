def solution(s):
    s = 'try hello world'
    ls = s.split(' ')
    answer = []
    for i in ls:
        ans = ''
        for j in range(len(i)):
            if j % 2 != 0:
                ans += i[j].upper()
            else:
                ans += i[j].lower()
        answer.append(ans)

    return ''.join(answer)
