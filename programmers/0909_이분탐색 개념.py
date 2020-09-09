'''
[바이너리 서치 - 이진탐색 (binary search)]
 1. 정의 및 특징
  - BigO : O(log N)
  - 정렬된 자료를 반으로 나누어 탐색하는 방법
  - 주의점 : ** 자료는 오름차순 으로 정렬된 자료여야 한다. **
  - 퍼포먼스가 아주 좋고 구현하는 중에 dynamic programming, recursion가 날 수 있다.

 2. 구현을 위한 준비
  - target : 찾고자 하는 값
  - data : 오름차순으로 정렬된 list
  - start : data 의 처음 값 인덱스
  - end : data 의 마지막 값 인덱스
  - mid : start, end 의 중간 인덱스

 3. 구현 개요
  - 자료의 중간 값이 (mid) 찾고자 하는 값인지 검사
  - 아니라면 대소관계를 비교하여 start, end 값 이동
  - 동일 연산 반복 (재귀로 구현 가능)

'''

# 이진탐색 구현 : data 중에서 target의 index 값을, 없으면 None을 return 한다.
def binary_search(target, data):
    data.sort()  # 무조건 정렬된 리스트
    start = 0
    end = len(data) - 1

    while start <= end:
        mid = (start + end) // 2

        if data[mid] == target:
            return mid   # 함수를 끝내버린다.
        elif data[mid] < target:
            start = mid + 1
        else:
            end = mid -1

    return None

# 이진탐색 구현(재귀 이용)
def binary_search_recursion(target, start, end, data):
    if start > end:
        return None

    mid = (start + end) // 2

    if data[mid] == target:
        return mid
    elif data[mid] > target:
        end = mid - 1
    else:
        start = mid + 1

    return binary_search_recursion(target, start, end, data)