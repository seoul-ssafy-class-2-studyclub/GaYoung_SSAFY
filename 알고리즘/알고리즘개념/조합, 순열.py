# [순열 계산 시 n개 모두 나오게하기]
'''
1. comb안에 for문 돌리기
   comb함수 안에 for n in range(len(data)+1)을 하면, result에 반복 되는 값이 엄청 많다!
   why? arr갯수가 n이면 result에 추가하고, n이 아니면 else에 계속 값이 들어간다.
'''

result = []
def comb(arr, k):
    for n in range(len(data)+1):
        if len(arr) == n:
            result.append(arr)

        else:
            for idx in range(k+1, len(data)):
               comb(arr + [data[idx]], idx)

for t in range(int(input())):
    N = int(input())
    data = list(map(int, input().split()))
    comb([], -1)
    print(result)  # 거의 시간초과급..


'''
2. comb([], -1) 위에 for문 돌리기
   n을 설정해주고, comb함수를 돌기 때문에 result에 필요한 값만 append된다.
'''
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
    for n in range(len(data) + 1):
        comb([], -1)
    print(result)