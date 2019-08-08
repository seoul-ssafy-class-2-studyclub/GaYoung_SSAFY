for t in range(int(input())):
    N = int(input())
    data = list(map(int, input().split()))
    for i in data:
        for j in range(1, 6):
            a = data.pop(0)-j
            if a >= 0:
                data.append(a)
            print(data)