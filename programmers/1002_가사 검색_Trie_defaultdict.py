'''
[트라이 자료구조]
 - dict 안에 dict 안에 dict 안에 dict,, 구조
 - 5:길이가 5인 단어, 6:길이가 6인 단어
'''
{5: {'f': [4,  # 5 : 길이가 5인 단어, 4: f로 시작하는 단어 4개
          {'r': [4,  # 4: r로 시작하는 단어 4개
                 {'o': [3,
                       {'d': [1,
                              {'o': [1,
                                     {}]}],
                        'n': [1,
                              {'t': [1,
                                     {}]}],
                        's': [1,
                              {'t': [1,
                                     {}]}],
                  'a': [
                      {'m': [1,
                             {'e': [1,
                                    {}]}]}]}]}]}],
     'k': [1,
           {'a': [1,
                  {'k': [1,
                         {'a': [1,
                                {'o': [1,
                                       {}]}]}]}]}]},
 6: {'f':[1,
          {'r':[1,
                {'o': [1,
                       {'z': [1,
                              {'e': [1,
                                     {'n': [1,
                                            {}]}]}]}]}]}]}
 }
'''
1. 만약 'fro??' 을 찾는다고 하자
 (1) 길이가 5 인 곳으로 들어간다
 (2) 거기서 f 로 들어간다. cnt에는 f로 시작하는 단어가 4개있다는 것을 저장한다.
 (3) r 로 들어간다. cnt에는 r로 시작하는 단어가 4개 있다는 것을 저장한다.
 (4) o 로 들어간다. cnt에는 o로 시작하는 단어가 3개 있다는 것을 저장한다.
 (5) ? 를 만나면 cnt 를 리턴.
 (6) fro 로 시작하면서 길이가 5인 단어는 마지막에 저장된 3개이다.
2. 문제점 : 이렇게 하면 효율성 3번에서 틀린다! why? 쿼리가 모두 ?로 구성된 경우 있음
   해결책 : 단어의 길이가 최대 1만까지이므로 1만까지의 배열을 만들고, 각 단어의 길이마다 몇개인지 저장
           쿼리가 모두 ?로 구성 -> 찾지말고 리스트에 저장해둔 갯수 꺼내기 ex.5, 6
'''

from collections import defaultdict
from collections import deque

def insert(part_trie, word):
    copy_trie = part_trie
    q = deque(list(word))

    while q:

        char = q.popleft()

        if char not in copy_trie:
            copy_trie[char] = [0, {}]
        copy_trie[char][0] += 1
        copy_trie = copy_trie[char][1]


def find(trie, query):
    cnt = 0
    copy_trie = trie
    if len(copy_trie) == 0:
        return 0

    q = deque(list(query))

    while q:
        char = q.popleft()
        if char == "?":
            return cnt
        else:
            if char not in copy_trie:
                return 0
            cnt = copy_trie[char][0]
            copy_trie = copy_trie[char][1]

    return cnt


def solution(words, queries):
    answer = []

    # 트라이 자료구조 활용하기
    trie = defaultdict(dict)
    reversed_trie = defaultdict(dict)

    # query가 모두 ?이면 시간초과 발생 -> 문자 길이에 따라 갯수 저장
    length_list = [0] * 10001

    # trie만들기
    for word in words:
        length_word = len(word)
        length_list[length_word] += 1

        insert(trie[length_word], word)
        insert(reversed_trie[length_word], word[::-1])

    # 찾기
    for query in queries:
        length_query = len(query)

        if query.count('?') == length_query:  # 쿼리가 모두 물음표인 경우
            answer.append(length_list[length_query])
            continue
        if query[0] == "?":  # 물음표로 시작하는 쿼리
            answer.append(find(reversed_trie[length_query], query[::-1]))
        else:
            answer.append(find(trie[length_query], query))


    return answer


words = ["frodo", "front", "frost", "frozen", "frame", "kakao"]
queries = ["fro??", "????o", "fr???", "fro???", "pro?"]
print(solution(words, queries))

