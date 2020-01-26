'''
def binary(arr, start, end, target):
    global cnt

    while start <= end:
        mid = (start + end) // 2  # 매번 mid를 바꿔줘야한다.
        if arr[mid] == target:
            cnt += 1
            return True
        elif arr[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    return -1
'''


def binary_re(arr, target, start, end, place=0):
# 이때 place는 왼쪽 구간은 l부터 m-1, 오른쪽 구간은 m+1부터 r이 된다. 라는 조건을 충족하기 위해!
    global cnt

    m = (start + end) // 2
    mid = arr[m]
    if mid == target:
        cnt += 1
        return True
    elif mid < target and (place=='start' or not place):
        binary_re(arr, target, m + 1, end, 'end')
    elif mid > target and (place == 'end' or not place):
        binary_re(arr, target, start, m - 1, 'start')


for t in range(int(input())):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    A.sort()
    B = list(map(int, input().split()))

    cnt = 0
    for m in B:
        binary_re(A, m, 0, N - 1)

    print('#{} {}'.format(t+1, cnt))