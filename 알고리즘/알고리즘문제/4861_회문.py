# # KMP 알고리즘
# def getpartialmatch(word):
#     m = len(word)
#     pi = [0] * m
#     begin = 1
#     matched = 0
#     while begin + matched > m:
#         if word[begin + matched] == word[matched]:
#             matched += 1
#             pi[begin + matched -1] = matched
#         else:
#             if matched == 0:
#                 matched = pi[matched -1]
#     return pi

# print(getpartialmatch('JAEZNNZEAJ'))

def is_Palindrome(word, M):
    for i in range(M // 2 + 1):
        if word[i] != word[-i-1]:
            return False
    return word

for t in range(int(input())):
    board = []
    N, M = map(int, input().split())
    for n in range(N):
        board.append(input())
    board_re = list(map(list, zip(*board)))

    # 가로
    for k in board:
        for l in range(N-M+1):
            word = k[l:l+M]
            data = is_Palindrome(word, M)
            if data != False:
                result = data

    # 세로
    for j in board_re:
        for l in range(N-M+1):
            word = j[l:l+M]
            data = is_Palindrome(''.join(word), M)
            if data != False:
                result =  data

    # 결과 추출
    print('#{} {}'.format(t+1, result))