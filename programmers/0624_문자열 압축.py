
s = 'aabbaccc'
# s = 'ababcdcdababcdcd'
# s = 'abcabcdede'
# s = 'abcabcabcabcdededededede'
# s = 'xababcdcdababcdcd'

'''
aabbaccc를 1, 2, 3,,, 처럼 하나씩 늘려가면서 합칠 수 있으면 합치기
  ex. 1이면 2a2ba3c, 2이상이면 없음
  각 알파벳마다 하나씩 늘려갈 때 cnt += 1해주고(새로운 알파벳 시작할 때마다 cnt=1이여야함)
  result에 가능한 답들을 넣고 최소값 구하기
'''
def solution(s):

    if len(s) == 1:
        return 1

    answer = 9999999999999999999999999999999
    for i in range(1, len(s) // 2 + 1):
        cnt = 1
        word = ''
        front = s[:i]  # 문자열은 제일 앞부터 정해진 길이만큼 잘라야 한다!
        for j in range(i, len(s) + i, i):
            back = s[j:j + i]
            if front == back:
                cnt += 1
            else:
                if cnt == 1:
                    word += front
                else:
                    word += str(cnt)
                    word += front
                    cnt = 1

            front = s[j:j + i]
        temp = len(word)
        if answer > temp:
            answer = temp

    return answer

# len(s) > 1일 때
'''
s = abcdabcd 이면 2abcd -> i는 1~4까지 진행하고 그 뒤에값이랑 비교
s = aaaaaaa 이면?? 7a
'''

'''
[신경 써야 하는 곳]
1. s[j:j+1] -> s[j:j+i] : 이렇게 되어야 j가 i만큼 띄어서 진행하는데, 다음 j전까지 값을 가질 수 있다.
                        : 문자열이 1개 단위로 잘릴 때는 상관없지만, 2개 이상이면 나오지 않음

2. for i in range(1, len(s) // 2 + 1) : 굳이 len(s)까지 할 필요가 없다.

3. for j in range(i, len(s) + i, i) : len(s) + i 하는 이유는 aabbaccc인 경우에 

'''

