# 1. hash사용
# hash는 dictionary처럼쓰는데, 실행할때마다 key값에 새로운 숫자를 제공
# ex. {1543287362802119979: 'leo', -599470287568687192: 'kiki', -5395674906811354268: 'eden'}
#     {8023414173644665412: 'leo', -2114411684575497391: 'kiki', 6585220722842758562: 'eden'}
# -> 저장된 주소를 알려준다고 생각하면 될듯
def solution(participant, completion):
    dic = {}
    res = 0
    for part in participant:
        dic[hash(part)] = part
        res += hash(part)

    for com in completion:
        res -= hash(com)
    ans = dic[res]  # key값을 넣은거니까 value값(이름)이 나온다

    return ans


# 2. Counter()는 dict와 같이 hash형 자료들의 값의 개수를 셀 때 사용
import collections

def cnt(participant, completion):
    # ans = collections.Counter(participant)  # Counter({'mislav': 2, 'stanko': 1, 'ana': 1})
    res = collections.Counter(participant) - collections.Counter(completion)  # Counter({'mislav': 1})

    return list(res.keys())[0]


# 3. sort이용
def use_sort(participant, completion):
    participant.sort()
    completion.sort()
    for i in range(len(completion)):
        if participant[i] != completion[i]:
            return participant[i]
        else:
            return participant[len(participant)-1]


# 4. zip 사용
def use_zip(participant, completion):
    participant.sort()
    completion.sort()
    pair = list(zip(participant, completion))
    # [('ana', 'ana'), ('mislav', 'mislav'), ('mislav', 'stanko')] -> 이런식으로 나오기때문에, sort를 해줘야한다
    for p, c in pair:
        if p != c:
            return p

    return participant[-1]
