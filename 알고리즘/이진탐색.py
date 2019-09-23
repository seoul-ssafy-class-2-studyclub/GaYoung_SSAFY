'''
이진탐색 (이진트리, 바이너리서치 중요!)

1. linear search(순차검색): 정렬방식 상관없음
2. binary search(이진탐색): 반드시 오름차순으로 정렬된 상태에서 시작!
시간속도: O(log N)


검색과정
1. 자료의 중앙에 있는 원소를 고른다.
2. 중앙 원소 값과 찾고자하는 목표 값을 비교한다.
3. 목표 값이 중앙 원소의 값보다 작으면, 자료의 왼쪽 반에 대해서 새로 검색을 수행하고,
   크다면 자료의 오른쪽 반에 대해서 새로 검색을 수행한다.
4. 찾고자 하는 값을 찾을때까지 1~3 과정을 반복한다.


ex. 이진 검색으로 7을 찾는 경우
2  4  7  9  11  19  23
검색범위 mid 검색제외범위 (why? 7 < mid=9)
2  4  7  9  11  19  23
  mid (7 > mid=4 -> 오른쪽 검색 -> start = mid + 1로 되어 새로운 검색 범위 지정)
'''


# 이진탐색 반복구조
def binary(arr, target):

    arr.sort()  # 이진탐색은 오름차순으로 정렬되어있어야 한다.
    start = 0
    end = len(arr) - 1  # arr의 마지막값의 index

    while start <= end:
        mid = (start + end) // 2  # 매번 mid를 바꿔줘야한다.
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    return -1


# 이진탐색 재귀사용
def binary_re(arr, target, start, end):

    while start <= end:
        mid = (start + end) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
        return binary_re(arr, target, start, end)
          # start, end를 함수 안에 적어주면 안됨 -> why? 재귀돌리면서 계속 초기화됨!
    return -1

arr = [1, 5, 7, 10, 25, 32, 79, 80, 125]
start = 0
end = len(arr) - 1
print(binary_re(arr, 7, start, end))
print(binary(arr, 8))