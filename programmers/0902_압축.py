def solution(msg):
    answer = []
    return answer

msg = 'KAKAO'
# msg = 'TOBEORNOTTOBEORTOBEORNOT'
# msg = 'ABABABABABABABAB'

dictionary = {}
for i in enumerate('ABCDEFGHIJKLMNOPQRSTUVWXYZ', 1):
    dictionary[i[1]] = i[0]



last_index = len(dictionary)
answer = []
for i in range(len(msg) - 1):
    if msg[i] in dictionary:
        answer.append(dictionary[msg[i]])
        wc = msg[i] + msg[i + 1]
        if wc not in dictionary:
            last_index += 1
            dictionary[wc] = last_index

print(dictionary)