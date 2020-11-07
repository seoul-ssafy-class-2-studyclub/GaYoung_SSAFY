def solution(penter, pexit, pescape, data):
    answer = ''
    res = []
    split_len = len(penter)
    start = 0
    for i in range(split_len - 1, len(data), split_len):
        res.append(data[start:i + 1])
        start = i + 1

    check = [penter, pexit, pescape]
    for i in res:
        if i in check:
            answer += pescape + i
        else:
            answer += i

    return penter + answer + pexit