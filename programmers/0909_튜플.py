def solution(s):
    s = s[2:-2].split('},{')
    s = sorted(s, key=lambda x: len(x))

    result = []
    for i in s:
        res = list(i.split(','))

        if len(i) == 1:
            result.append(int(res[0]))

        else:
            for j in res:  # j는 str
                if int(j) not in result:  # 비교할때에도 int(j)라고 해야함
                    result.append(int(j))

    # print(result)
    return result

# s = '{{2},{2,1},{2,1,3},{2,1,3,4}}'
s = '{{1,2,3},{2,1},{1,2,4,3},{2}}'
# s = '{{20,111},{111}}'
# s = '{{123}}'
# s = '{{4,2,3},{3},{2,3,4,1},{2,3}}'

