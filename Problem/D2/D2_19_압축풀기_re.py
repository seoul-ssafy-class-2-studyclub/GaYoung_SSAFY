for t in range(int(input())):
    N = int(input())
    data = ''
    for n in range(N):
        word, num = input().split()
        data += word * int(num)  # AAAAAAAAAABBBBBBBCCCCC

    print('#{}'.format(t + 1))
    for d in range(len(data)):
        print(data[d], end='')
        if (d + 1) % 10 == 0:
            print('')
