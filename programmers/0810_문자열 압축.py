# s = 'aabbaccc'  # 1개 단위 : 2a2ba3c
# s = 'ababcdcdababcdcd'  # 8개 단위 : 2ababcdcd
'''
1개 ababcdcdababcdcd
2개 2ab2cd2ab2cd
8개 2ababcdcd
'''
# s = 'abcabcdede'
# s = 'abcabcabcabcdededededede'
# s = 'xababcdcdababcdcd'
s = 'ab'


'''
** 문제점 : 맨 앞에 aabbacc일 때 맨 앞에 2a가 들어와야하는데 두번째 a부터 들어온다 
for i in range(1, len(s)):  # for i in range(1, len(s)):, 
    temp = ''
    cnt = 1
    front = s[:i]
    for j in range(i+1, len(s), i):
        ss = s[j:j+i]


** 해결책
for i in range(1, len(s)):  # for i in range(1, len(s)):, 
    temp = ''
    cnt = 1
    front = s[:i]
    for j in range(i, len(s), i):
        ss = s[j:j+i]
'''
def solution(s):
    ans = 999999999999999999999999999999

    if len(s) == 1:
        return 1

    for i in range(1, len(s) // 2 + 1):  # len(s)의 반만 돌아도 괜찮다. 어차피 최대가 2s의반
        temp = ''
        cnt = 1
        front = s[:i]
        for j in range(i, len(s) + i, i):
            # 여기서 len(s)를 하면 aabbaccc에서 2a2ba까지 나오고 3c가 나오지 않음.
            # why? j가 i만큼 건너뛰면서 나타나는데 이때 끝까지 가지 못해서임
            ss = s[j:j + i]

            if front == ss:
                cnt += 1

            else:
                if cnt == 1:
                    temp += front
                else:
                    temp += str(cnt) + front
                cnt = 1  # aabbacc에서 2a3b로 나왔다. 이는 cnt가 제때 갱신이 되지 않아서임

            front = ss  # 앞에 값을 뒤의 값으로 바꿔줘야 그 뒤에값이랑 비교해나갈 수 있다.

        if ans > len(temp):
            ans = len(temp)

    # print(ans)

    return ans

print(solution(s))