'''
링크드 리스트 사용 -> 파이썬은 슬라이싱해서 끼워넣을 수 있음(중간에도 넣을 수 있음)
                 -> 이 자체가 linked list
append, pop 사용하면 시간초과
'''


def merge_sort(arr):  # arr = [14, 7, 3, 12, 9, 11, 6, 2]
    if len(arr) == 1:  # arr = [2] -> 결과 : arr
        return arr  # 탈출조건

    else:
        mid = len(arr) // 2   # arr의 중간 찾기
        right = arr[mid:]   #  분할
        left = arr[:mid]

        l = merge_sort(left)  # 정복
        r = merge_sort(right)
        return merge(l, r)  # 결합

'''
merge algorithm
8  7  6  5    4  3  2  1
 78    56      34    12
 i     j       i     j
   5678          1234
   i             j
        12345678
'''


'''
N//2 번째 원소와 오른쪽 원소가 먼저 복사되는 경우의 수
merging하는 과정에서 left right를 result에 넣기 전에
left[-1], right[-1]을 비교해서
left[-1]이 더 큰 경우, right[-1]이 자리를 바꿔야함으로 먼저 복사됨 counting
'''


def merge(left, right):
    global cnt
    sorted_list = []
    i = j = 0

    if left[-1] > right[-1]:
        cnt += 1

    while len(left) > i and len(right) > j:
        if left[i] > right[j]:
            sorted_list.append(right[j])
            j += 1
        else:
            sorted_list.append(left[i])
            i += 1

    while len(left) > i:
        sorted_list.append(left[i])
        i += 1

    while len(right) > j:
        sorted_list.append(right[j])
        j += 1

    return sorted_list


for t in range(int(input())):
    N = int(input())
    data = list(map(int, input().split()))
    cnt = 0
    result = merge_sort(data)
    print('#{} {} {}'.format(t+1, result[N//2], cnt))