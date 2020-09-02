relation = [["100","ryan","music","2"],
            ["200","apeach","math","2"],
            ["300","tube","computer","3"],
            ["400","con","computer","4"],
            ["500","muzi","music","3"],
            ["600","apeach","music","2"]]

from itertools import combinations
from copy import deepcopy

def solution(relation):
    def unique(row, co):
        '''
        [원래 계획]
        use에 사용한 co를 넣고, 그것이 포함되어있는 co는 지운다.
        check = []
        for item in relation:
            for idx in co:
                check.append(tuple(item[idx]))
                use.append(co)

        # [('1', '0', '0'), ('2', '0', '0'), ('3', '0', '0'), ('4', '0', '0'), ('5', '0', '0'), ('6', '0', '0')]
        # 이렇게 나온다. 내가 원하는것은 [('100', 'ryan', 'music'), ('200', 'apeach', 'math'), ('300', 'tube', 'computer'), ('400', 'con', 'computer'), ('500', 'muzi', 'music'), ('600', 'apeach', 'music')]
        '''

        '''
        [수정방안 1]
        check = []  # [('100', 'ryan', 'music'), ('200', 'apeach', 'math'), ('300', 'tube', 'computer'), ('400', 'con', 'computer'), ('500', 'muzi', 'music'), ('600', 'apeach', 'music')]
        for item in relation:
            check.append(tuple(item[idx] for idx in co))
        # 이렇게 하면 내가 원하는대로 나오지만, 따로 해당 co를뺄 수 없다.

        use = []
        check = []  # [('100', 'ryan', 'music'), ('200', 'apeach', 'math'), ('300', 'tube', 'computer'), ('400', 'con', 'computer'), ('500', 'muzi', 'music'), ('600', 'apeach', 'music')]
        for item in relation:
            check.append(tuple(item[idx] for idx in co))

            if co not in use:
                use.append(co)
        print(use)

        이렇게 식을 작성해버리면 use에 쌓이지 않고 [(0,)], [(1,)], [(2,)], [(3,)], [(0, 1)]이런 식으로 나와버린다.


        [수정방안 2]
        unique에 해당하는 use를 다 넣어버리고나서 나중에 중복이 있는지 확인한다. -> 최종채택
        '''
        check = []  # [('100', 'ryan', 'music'), ('200', 'apeach', 'math'), ('300', 'tube', 'computer'), ('400', 'con', 'computer'), ('500', 'muzi', 'music'), ('600', 'apeach', 'music')]
        for item in relation:
            check.append(tuple(item[idx] for idx in co))

        # (0, ), (0, 1), (0, 1, 2)인 경우를 [(relation[0]), (relation[0], relation[1]), (relation[0], relation[1], relation[2])]이런식으로 한번에 넣고싶으면, tuple로 묶어서 넣어라
        if len(set(check)) == row:
            return True

        return False

    row = len(relation)
    column = len(relation[0])
    columns = [i for i in range(column)]

    use = []
    for i in range(1, column + 1):
        comb = list(combinations(columns, i))
        for co in comb:  # co = (0,), (1,), (2,), (3,), (0, 1)
            if unique(row, co):
                use.append(co)

    # print(use)  # [(0,), (0, 1), (0, 2), (0, 3), (1, 2), (0, 1, 2), (0, 1, 3), (0, 2, 3), (1, 2, 3), (0, 1, 2, 3)]

    '''
    [중복 확인 방법]
    1. issubset을 사용해(only set일때 사용가능) -> set(use[i])가 set(use[j])의 부분집합이 된다면 지워라!
       - ** 문제점 : 지우면 index가 달라져서 에러,,
       - ** 해결책 : 
       
    2. visit으로 확인하고 방문하지 않은 애들만 갯수를 센다 0 -> 현재 내가 사용한 방법 
    '''
    visit = [0] * len(use)
    for i in range(len(use)):
        for j in range(i + 1, len(use)):
            # print(use_copy[i], use_copy[j])
            if set(use[i]).issubset(set(use[j])):
                visit[j] = 1

    cnt = 0
    for i in visit:
        if i == 0:
            cnt += 1

    return cnt

use = [(0,), (0, 1), (0, 2), (0, 3), (1, 2), (0, 1, 2), (0, 1, 3), (0, 2, 3), (1, 2, 3), (0, 1, 2, 3)]
use_copy = deepcopy(use)

for i in range(len(use)):
    for j in range(i + 1, len(use)):
        if use[i] == use[i] & use[j]:
            use.remove(use[j])
