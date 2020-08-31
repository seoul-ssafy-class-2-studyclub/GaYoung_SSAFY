# s = "{{2},{2,1},{2,1,3},{2,1,3,4}}"  # [2, 1, 3, 4]
s = "{{1,2,3},{2,1},{1,2,4,3},{2}}"  # [2, 1, 3, 4]
# s = "{{20,111},{111}}"  # [111, 20]
# s = "{{123}}"  # [123]
# s = "{{4,2,3},{3},{2,3,4,1},{2,3}}"  # [3, 2, 4, 1]

def solution(s):
    result = []
    # 원래 s[1:-1].split(',')해서 할랬는데,
    # ['{20', '111}', '{111}']이렇게 나와서 뽑아내야하는게 많아져서 s = s[2:-2].split('},{')
    ss = s[2:-2].split('},{')  # ['20,111', '111']
    sss = sorted(ss, key=lambda x: len(x))
    print(sss)

    for i in sss:
        res = list(i.split(','))  # '20, 111'인 경우 [20, 111]로 잘라야함

        if len(res) == 1:
            result = [int(res[0])]

        else:
            print(result)
            for r in res:
                if int(r) not in result:
                    result.append(int(r))
    print(result)

    return result





# 다른 풀이 -> 원소의 갯수가 가장 많은 순서대로 리스트에 담기
import re
from collections import Counter

def solution1(s):

    s = Counter(re.findall('\d+', s))  # \d+ : 숫자 -> # Counter({'2': 4, '1': 3, '3': 2, '4': 1})
    ss = sorted(s.items())  # [('1', 3), ('2', 4), ('3', 2), ('4', 1)]

    return list(map(int, [k for k, v in sorted(ss, key=lambda x: x[1], reverse=True)]))



print(solution1(s))