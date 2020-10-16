def solution(genres, plays):
    music = {}
    check = {}
    for i in range(len(genres)):
        if genres[i] not in music:
            music[genres[i]] = plays[i]
            check[genres[i]] = [[plays[i], i]]
        else:
            music[genres[i]] += plays[i]
            check[genres[i]].append([plays[i], i])

    music = sorted(music.items(), key=lambda x:x[1], reverse=True)

    answer = []
    for name, count in music:
        if len(check[name]) == 1:
            answer.append(check[name][0][1])
        elif len(check[name]) >= 2:
            check[name] = sorted(check[name], key=lambda x: x[0], reverse=True)

            for i in range(2):
                answer.append(check[name][i][1])
    # print(answer)
    return answer

# genres = ['classic', 'pop', 'classic', 'classic', 'pop']
# plays = [500, 600, 800, 800, 2500]

genres = ['classic', 'pop', 'classic', 'classic', 'pop', 'jaze']
plays = [500, 600, 501, 800, 900, 100]  # [3, 2, 4, 1]
print(solution(genres, plays))