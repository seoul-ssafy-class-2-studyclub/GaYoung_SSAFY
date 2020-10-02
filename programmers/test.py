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
    # 트라이 자료구조 활용하기!
    trie = defaultdict(dict)
    reversed_trie = defaultdict(dict)

    # !!!쿼리가 모두 물음표인 경우 시간 초과가 발생하므로, 문자 길이에 따라 갯수 저장
    length_list = [0] * 10001

    # trie 만들기
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
