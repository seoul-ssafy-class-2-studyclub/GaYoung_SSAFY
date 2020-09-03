def solution(s):

    # len(s) == 1일때를 따로 빼주는 이유 : len(s) == 1이면 for문을 돌 수 없다. range가 올바르지 못함
    if len(s) == 1:
        return 1

    mymin = 999999999999999999999999999999999999
    for i in range(1, len(s) // 2 + 1):
        front = s[:i]
        cnt = 1
        word = ''

        # len(s)+i인 이유 -> len(s)하면 s='aabbaccc'이고 i=4이면 j=4,8인데,
        # len(s)로 두면 j=4만 가능함 -> len(s)+1하면 i=3일때, aabbac까지만 나온다
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

            front = back

        res = len(word)
        if mymin > res:
            mymin = res

    return mymin

s = 'aabbaccc'
# s = 'ababcdcdababcdcd'
# s = 'abcabcdede'
# s = 'abcabcabcabcdededededede'
# s = 'xababcdcdababcdcd'


