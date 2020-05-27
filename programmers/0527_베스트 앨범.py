genres = ['classic', 'pop', 'classic', 'classic', 'pop']
plays = [500, 600, 500, 800, 2500]

def solution(genres, plays):

    genres_dict = {genres[0]:[(plays[0], 0)]}
    total_dict = {genres[0]:plays[0]}
    ans = []

    if len(genres) > 1:
        for i in range(1, len(genres)):
            if genres[i] not in genres_dict:
                genres_dict[genres[i]] = [(plays[i], i)]
                total_dict[genres[i]] = plays[i]

            else:
                genres_dict[genres[i]].append((plays[i], i))
                total_dict[genres[i]] += plays[i]

    # genres_dict = {'classic': [(500, 0), (150, 2), (800, 3)], 'pop': [(600, 1), (2500, 4)]}
    # total_dict = {'classic': 1450, 'pop': 3100}

    # total_dict의 값이 큰 순서대로 genres_dict에 가서 2개씩 뽑아낸다

        total_dict_value = []
        for i in total_dict.values():
            total_dict_value.append(i)

        ls = sorted(total_dict_value,reverse=True)  # [3100, 1450]

        # 하고 싶은 것 : 3100을 가진 total_dict의 key값을 이용해 genres_dict의 value 중에서 큰 값 두개를 가지고온다.


        for l in ls:
            # print(total_dict.items())
            for key, value in total_dict.items():
                # print(key, value)
                if value == l:
                    # print('yes')
                    flag = genres_dict[key]
                    # print(flag)
                    flag_res = sorted(flag, reverse=True)
                    # print(flag_res)

                    # 재생 수가 같으면 index가 작은 것부터 하기위해서 이 과정을 추가
                    for i in range(len(flag_res)-1):
                        if flag_res[i][0] == flag_res[i+1][0]:
                            if flag_res[i][1] > flag_res[i+1][1]:
                                flag_res[i], flag_res[i+1] = flag_res[i+1], flag_res[i]
                                # print(flag_res[i], flag_res[i + 1])

                    if len(flag_res) >= 2:  # 이때 재생 수가 같으면 index가 작은 것부터
                        for i in range(2):
                            ans.append(flag_res[i][1])
                    else:
                        for i in range(len(flag_res)):
                            ans.append(flag_res[i][1])
    else:
        ans.append(0)
    # print(ans)

    return ans

# solution(genres,plays)

