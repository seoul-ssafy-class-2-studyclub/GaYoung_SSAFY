from collections import deque

def solution(begin, target, words):

    if target not in words:
        return 0

    queue = deque([begin])

    answer = 0
    while len(words):
        for q in queue:
            temp = []
            for word in words:
                cnt = 0
                for i in range(len(word)):
                    if q[i] != word[i]:
                        cnt += 1

                        if cnt == 2:
                            break

                if cnt == 1:
                    temp.append(word)
                    words.remove(word)

        answer += 1
        if target in temp:
            break
        else:
            queue = temp

    return answer

begin = 'hit'
target = 'cog'
words = ['hot', 'dot', 'dog', 'lot', 'log', 'cog']

# begin = 'hit'
# target = 'cog'
# words = ['hot', 'dot', 'dog', 'lot', 'log']
