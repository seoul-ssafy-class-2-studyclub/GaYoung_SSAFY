# A = ['abc', 'bca', 'dbe']
# A = ['zzzz', 'ferz', 'zdsr', 'fgtd']
S = ['gr', 'sd', 'rg']

def solution(S):
    answer = []
    length = len(S[0])
    for i in range(len(S)):
        for j in range(i+1, len(S)):
            for num in range(length):
                if answer:
                    print('stop')
                    break
                else:
                    print('find')
                    if S[i][num] == S[j][num]:
                        answer.append([i, j, num])

    if answer:
        return answer[0]
    else:
        return answer

print(solution(S))