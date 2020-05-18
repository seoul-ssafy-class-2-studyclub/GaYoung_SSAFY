def solution(s):
    
    # len(s) == 1이면 for i in range(1, len(s) // 2 + 1)에 포함이 안됨
    # 따로 빼야함
    if len(s) == 1:
        return 1
    
    ans = 99999999999999999999
    # len(s)//2+1을 한 이유? -> 한번에 최대한 많은 글자가 중복이 되려면 최대 반이다
    # ex. ababcdababcd이면 ababcd일때 한번에 최대한 많은 글자가 중복이 됨
    for i in range(1, len(s) // 2 + 1):
        word = ''
        cnt = 1
        front = s[:i]

        # len(s)+i인 이유 -> len(s)하면 s='aabbaccc'이고 i=4이면 j=4,8인데,
        # len(s)로 두면 j=4만 가능함 -> len(s)+1하면 i=3일때, aabbac까지만 나온다
        for j in range(i, len(s) + i, i):
            if front == s[j:j + i]:
                cnt += 1
            else:
                if cnt == 1:
                    word += front
                else:
                    word += str(cnt)
                    word += front
                    cnt = 1  # cnt 초기화
            front = s[j:j + i]  # front값을 계속 바꿔주기

        res = len(word)
        if ans > res:
            ans = res

    return ans


s = 'aabbaccc'
'''
2a2ba3c -> 7
2a2baccc
aabba3c
'''

# s = 'ababcdcdababcdcd'
'''
ababcdcdababcdcd
2ab2cd2ab2cd
2ababcdcd -> 9
'''
# s = 'abcabcdede'
# s = 'abcabcabcabcdededededede'
# s = 'xababcdcdababcdcd'


