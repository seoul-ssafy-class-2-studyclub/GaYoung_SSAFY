# s = "{{2},{2,1},{2,1,3},{2,1,3,4}}"
# s = "{{1,2,3},{2,1},{1,2,4,3},{2}}"
# s = "{{20,111},{111}}"
# s = "{{123}}"
s = "{{4,2,3},{3},{2,3,4,1},{2,3}}"

def solution(s):
    answer = []
    s = s[2:-2].split('},{')
    s = sorted(s, key=lambda x:len(x))

    for i in s:
        i = list(i.split(','))

        if len(i) == 1:
            answer.append(int(i[0]))

        else:
            for j in i:
                if int(j) not in answer:
                    answer.append(int(j))

    # print(answer)
    return answer

print(solution(s))