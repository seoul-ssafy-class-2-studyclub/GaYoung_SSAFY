def solution(seoul):
    ans = '김서방은 '
    for i in range(len(seoul)):
        if seoul[i] == 'Kim':
            ans += str(i)
            ans += '에 있다'
            return ans


seoul = ['Jane', 'Kim']
