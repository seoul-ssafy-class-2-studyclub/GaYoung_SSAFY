'''런타임에러
result = []
def comb(arr, k):
    if len(arr) == n:
        result.append(arr)

    else:
        for idx in range(k+1, len(data)):
           comb(arr + [data[idx]], idx)

for t in range(int(input())):
    N = int(input())
    data = list(map(int, input().split()))
    for n in range(len(data) + 1):  # n을 설정해주고, comb함수를 돌기 때문에
        comb([], -1)

    rs = {0}
    for i in result:
        rs.add(sum(i))
    r = len(rs)
    print(r)
'''

# 방법1
def score(data):
    result = {0}
    for i in data:
        for j in list(result):
            result.add(i+j)
    return len(result)

for t in range(int(input())):
    N = int(input())
    data = list(map(int, input().split()))

    print('#{} {}'.format(t+1, score(data)))



# 방법2