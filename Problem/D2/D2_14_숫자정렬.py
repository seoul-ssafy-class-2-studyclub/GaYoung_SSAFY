for t in range(int(input())):
    N = int(input())
    data = list(map(int, input().split()))

    for k in range(N-1):
        for i in range(N-k-1):
            if data[i] > data[i+1]:
                data[i] , data[i+1] = data[i+1] , data[i]
                print(data)