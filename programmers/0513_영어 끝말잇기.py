# n = 3
# words = ['tank', 'kick', 'know', 'wheel', 'land', 'dream', 'mother', 'robot', 'tank']

# n = 5
# words = ['hello', 'observe', 'effect', 'take', 'either', 'recognize', 'encourage', 'ensure', 'establish', 'hang', 'gather', 'refer', 'reference', 'estimate', 'executive']

n = 2
words = ['hello', 'one', 'even', 'never', 'now', 'world', 'draw']


def solution(n, words):
    front = words[0]
    use_data = [front]
    for i in range(1, len(words)):
        # 끝말잇기가 말이 된다면 use_data에 넣고, front를 words[i]로 바꾸기
        # 글고 말이 된다해도 만약에 use_data안에 있었으면 진것
        if front[-1] == words[i][0]:
            if words[i] not in use_data:
                front = words[i]
                use_data.append(front)
            else:  # 단어 중복이면
                num = i % n + 1
                turn = i // n + 1
                return [num, turn]

        else: # 끝말잇기 말이 안된다면
            num = i % n + 1
            turn = i // n + 1
            return [num, turn]

    return [0,0]

print(solution(n, words))