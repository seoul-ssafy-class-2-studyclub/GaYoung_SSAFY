for t in range(int(input())):
    data = [list(input()) for _ in range(5)]

    word_list = []
    for i in data:
        if len(i) != 15:
            i = i + ['-1'] * (15-len(i))
        word_list.append(i)
    # print(word_list)

    result = []
    for j in range(15):
        for k in range(5):
            result += [word_list[k][j]]
    
    print('#{}'.format(t+1), end=' ')
    for l in result:
        if l == '-1':
            l = ''
        print(l, end='')
    print()
