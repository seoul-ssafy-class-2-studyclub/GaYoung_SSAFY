for t in range(int(input())):
    N = int(input())
    data = list(map(int, input().split()))
    scores = [0] * 101
    for i in range(1000):
        if data[i]:
            scores[data[i]] += 1
    # print(scores)
    result = []
    r = []
    for i in range(101):
        result.append([i, scores[i]])
    # print(result)
    for k in range(len(result)):
        # print(max(scores), result[k])
        if result[k][1] == max(scores):
            r.append(result[k][0])
    print(max(r))