def solution(s):

    if len(s) == 1:
        return 1

    len_s = len(s)
    mymin = 999999999999999999999999999
    for i in range(1, len_s // 2 + 1):  # 몇개단위로 볼 것인가 -> 글자수의 반만 보면 됨.
        front = s[:i]
        cnt = 1
        word = ''
        # s = "ababcdcdababcdcd"라면 i는 ababcdcd까지만 확인하면 됨.
        # j는 len(s) + i까지 확인해야한다. why? i만큼 더해야 i=8일때, j=8, 16으로 둘다 확인할 수 있다.
        # j가 그냥 len(s)라면 j=8이므로 뒤에 값까지 확인할 수 없다.
        for j in range(i, len_s + i, i):
            back = s[j:j + i]

            if front == back:
                cnt += 1

            else:
                if cnt == 1:
                    word += front
                else:
                    word += str(cnt) + front
                    cnt = 1

            front = back

        if mymin >= len(word):
            mymin = len(word)

    # print(mymin)

    return mymin

# s = "aabbaccc"  # 2a2ba3c
s = "ababcdcdababcdcd"  # 2: 2ab2cd2ab2cd, 8: 2ababcdcd
# s = "abcabcdede"
# s = "abcabcabcabcdededededede"
# s = "xababcdcdababcdcd"
