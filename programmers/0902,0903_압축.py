def solution(msg):
    answer = []
    return answer

# msg = 'KAKAO'
# msg = 'TOBEORNOTTOBEORTOBEORNOT'
msg = 'ABABABABABABABAB'

dictionary = {}
for i in enumerate('ABCDEFGHIJKLMNOPQRSTUVWXYZ', 1):
    dictionary[i[1]] = i[0]



last_index = len(dictionary)
answer = []
w = msg[0]
print('w')
print(w)
# for문으로 하게되면 dictionary에 w+c가 있다면, w=w+c, c=msg[i+1]로 해야하는데, 그러면 문제가있다...

for i in range(1, len(msg)):
    c = msg[i]

    if w+c not in dictionary:
        print('plus')
        answer.append(dictionary[w])
        last_index += 1
        dictionary[w+c] = last_index
        w = c
