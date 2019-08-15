for t in range(int(input())):
    N = int(input())
    word = ['.', '?', '!']
    data = input()
    result_word = []
    for i in range(len(data)):
        if data[i] in word:
            result_word += [i]

    result = []
    cnt = 0
    index_1 = 0
    for k in result_word:
        index_2 = k
        result += data[index_1:index_2]  # ['Annyung Hasae Yo', 'Annyung Hasae Yo! LoL']
        index_1 = index_2
    print(''.join(result))

    # for n in result:
    #     for i in range(len(n)):
    #         if result[i].istitle:
    #             cnt += 1
    # print(cnt)