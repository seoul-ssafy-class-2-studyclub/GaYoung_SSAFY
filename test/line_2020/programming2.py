def solution(ball, order):
    visit = [0] * len(order)
    result = []

    while True:
        if visit == [1] * len(order):
            break

        for i in range(len(order)):
            print(i)
            if order[i] == ball[0] and visit[i] == 0:
                visit[i] = 1
                result.append(order[i])
                ball.pop(0)
                break

            elif order[i] == ball[-1] and visit[i] == 0:
                visit[i] = 1
                result.append(order[i])
                ball.pop()
                break

    # print(result)
    return result

ball = [1, 2, 3, 4, 5, 6]
order = [6, 2, 5, 1, 4, 3]
# # result = [6, 5, 1, 2, 4, 3]

# ball = [11, 2, 9, 13, 24]
# order = [9, 2, 13, 24, 11]
# # result = [24, 13, 9, 2, 11]

print(solution(ball,order))