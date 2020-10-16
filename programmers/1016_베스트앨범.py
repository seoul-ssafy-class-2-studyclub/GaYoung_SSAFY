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
    # print(music)
    answer = []
    for mu in music:
        m = mu[0]
        if len(check[m]) == 1:
            answer.append(check[m][1])
        elif len(check[m]) >= 2:
            check[m] = sorted(check[m], key=lambda x: x[0], reverse=True)
            # check[m] = sorted(check[m], key=lambda x: x[0], reverse=True)
            print(check[m])
            for i in range(2):
                answer.append(check[m][i][1])
    # print(answer)
    return answer

# genres = ['classic', 'pop', 'classic', 'classic', 'pop']
# plays = [500, 600, 800, 800, 2500]

genres = ['classic', 'pop', 'classic', 'classic', 'pop']
plays = [500, 600, 501, 800, 900]
print(solution(genres, plays))