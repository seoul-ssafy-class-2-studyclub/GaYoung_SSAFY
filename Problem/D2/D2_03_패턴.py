for t in range(int(input())):
    data = input()
    result = []
    for i in range(1, 11):
        if data[0:i] == data[i:2*i]:
            result.append(i)
    print(f'#{t+1} {result[0]}')
