'''
분할정복 알고리즘
1. 분할: 원래 문제를 분할하여 비슷한 유형의 더 작은 하위 문제들로 나누세요.
         -> merge_sort()
2. 정복: 하위 문제 각각을 재귀적으로 해결하세요. 하위 문제의 규모가 충분히 작으면
         문제를 탈출 조건으로 놓고 해결하세요. -> left, right에서 더 나아가기!
3. 합치기: 하위 문제들의 답을 합쳐서 원래 문제를 해결하세요. -> merge()
'''


'''
merge_sort algorithm
        87654321
    8765        4321
   87  65      43  21
 8  7  6  5    4  3  2  1
n // 2로 나누고 1개씩의 요소가 남기까지 재귀뢰 사용
그 후, 그 다음에 2개씩의 요소들을 반복적으로 merge 한다(하나로 합침)
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
def merge(left, right):
    sorted_list = []
    i = 0
    j = 0
    while i < len(left) and j < len(right):
        if left[i] > right[j]:
            sorted_list.append(right[j])
            j += 1
        else:
            sorted_list.append(left[i])
            i += 1

    while i < len(left):
        sorted_list.append(left[i])
        i += 1

    while j < len(right):
        sorted_list.append(right[j])
        j += 1

    return sorted_list
