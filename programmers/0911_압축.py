def solution(msg):
    dictionary = {}
    for i in enumerate('ABCDEFGHIJKLMNOPQRSTUVWXYZ', 1):
        dictionary[i[1]] = i[0]

    last_idx = 27
    word = msg[0]

    answer = []
    for i in range(1, len(msg)):  # 1부터 시작하는 이유 : word=msg[0]이므로 그 다음값이랑 비교
        # 현재 + 다음 단어 없으면
        # 1. 현재 단어 배열에 넣고 2. 현재 + 다음단어 dictionary에 넣고 3. 다음단어 = 현재단어로 갱신
        if word + msg[i] not in dictionary:
            answer.append(dictionary[word])
            dictionary[word + msg[i]] = last_idx
            last_idx += 1
            word = msg[i]

        # 이미 dictionary에 값이 있으면, 다음 단어를 현재 입력에 추가한다.
        else:
            word = word + msg[i]

    # 마지막 글자 answer에 추가하기
    answer.append(dictionary[word])
    # print(answer)

    return answer

# msg = 'KAKAO'
# msg = 'TOBEORNOTTOBEORTOBEORNOT'
msg = 'ABABABABABABABAB'

