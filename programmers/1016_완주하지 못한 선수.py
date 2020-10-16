# dictionary 이용
def solution(participant, completion):
    check = {}
    for i in participant:
        if i not in check:
            check[i] = 1
        else:
            check[i] += 1

    for com in completion:
        check[com] -= 1
        if check[com] == 0:
            del check[com]

    for i in check:
        return i


# hash 사용 : key값에 새로운 숫자를 제공하므로 저장된 주소를 알려준다.
def solution(participant, completion):
    check = {}
    res = 0
    for i in participant:
        check[hash(i)] = i
        res += hash(i)

    for com in completion:
        res -= hash(com)

    return check[res]