'''
[트라이자료구조]
 - 트라이 자료구조에 가사 단어를 insert 할 때 각 알파벳마다 존재하는 count에 1씩 더해준다.
 - 이 때 와일드카드 문자가 모두 '?'일 수도 있으므로 트라이 자료구조 head의 count도 계속 1씩 더해준다.
 - 단어의 길이마다 각각 트라이 자료구조를 만들어줘야 한다.
'''

class Node:  # 형태가 5 : {'f' : [4, {'r': [3, ,,]}]}
    def __init__(self, data):
        self.data = data
        self.count = 0
        self.child = {}


class Trie:
    def __init__(self):
        self.head = Node(None)

    def insert(self, string):
        cur = self.head
        cur.count += 1

        for c in string:
            if c not in cur.child:
                cur.child[c] = Node(c)  # 자식이 없으면 만들어주기
            cur = cur.child[c]  # 부모바꿔주기
            cur.count += 1

    def count(self, prefix):
        cur = self.head

        for c in prefix:
            if c not in cur.child:
                return 0
            cur = cur.child[c]

        return cur.count


def create_trie(words, is_reversed=False):
    trie_dic = {i: Trie() for i in range(1, 10001)}

    for word in words:
        if is_reversed:
            word = word[::-1]
        trie_dic[len(word)].insert(word)

    return trie_dic


def count_matched_word(tries, reversed_tries, query):
    no_mark_query = query.replace('?', '')

    if query[0] == '?':
        return reversed_tries[len(query)].count(no_mark_query[::-1])
    else:
        return tries[len(query)].count(no_mark_query)


def solution(words, queries):
    answer = []

    tries = create_trie(words)
    reversed_tries = create_trie(words, True)

    for query in queries:
        answer.append(count_matched_word(tries, reversed_tries, query))

    return answer