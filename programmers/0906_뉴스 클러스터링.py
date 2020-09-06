
# str1 = 'FRANCE'
# str2 = 'french'

# str1 = 'handshake'
# str2 = 'shake hands'

str1 = 'aa1+aa2'
str2 = 'AAAA12'

# str1 = 'E=M*C^2'
# str2 = 'e=m*c^2'

def make_split(word):
    answer = []
    for i in range(len(word) - 1):
        w = word[i:i+2]
        if w.isalpha():
            answer.append(w.lower())

    return answer

def make_part(one, two):
    answer = []

    # str1과 str2의 값 중 str2의 원소 갯수가 많을 때만 정답 처리되도록 구현
    for a in range(len(one)):
        for b in range(len(two)):
            if one[a] == two[b]:
                answer.append(one[a])
                del two[b]  # two에서 지우지 않으면 one에 있어서 break한 값을 다시 확인하게됨
                break

    return answer


def solution(str1, str2):

    one = make_split(str1)
    two = make_split(str2)
    len_one = len(one)
    len_two = len(two)

    if len_one == 0 and len_two == 0:
        return 65536

    elif one == two:
        return 65536

    else:
        intersection = len(make_part(one, two))
        union = len_one + len_two - intersection

        return int(intersection / union * 65536)

print(solution(str1, str2))