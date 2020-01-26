def q_sort(l, r):  # 무조건 처음값과 마지막값을 비교
    if l < r:  #
        pivot = partition(l, r)  # pivot = 3
        if idx > pivot:  # idx = 3
            q_sort(pivot + 1, r)
        else:
            q_sort(l, pivot - 1)
'''
0  1  2  3  4  5
7  3  6  8  9  10
pivot=3, idx=3이므로 q_sort(l, pivot - 1)

idx=N//2 <= pivot이므로 pivot 앞의 숫자들을 정렬해줘야함 -> q_sort(0, 2)

if idx > pivot이면 pivot 뒤의 숫자들을 정렬해줘야함
'''



def partition(l, r):
    pivot = arr[r]  # 피봇은 언제나 arr의 마지막 값
    i = l - 1  # i = -1
    for j in range(l, r):  # j = 0 ~ N-2까지
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[r] = arr[r], arr[i + 1]
    return i + 1

'''
       정렬기준                pivot은 8이지만 새롭게 정렬할 기준은 | 이다
           |  0  1   2  3  4  5
           |  7  10  3  6  9  8
       i=-1|
j = 0 ~ N-2|

            10>8 -> if문에 들어가지 않음 -> action없음
             0 | 1  2  3  4  5
             7 |10  3  6  9  8
            i=0|
j = 0 ~ N-2    |j=1 -> arr[i + 1], arr[r] = arr[r], arr[i + 1]

            3<8 -> i+=1
             0  1 | 2  3  4  5
             7  10| 3  6  9  8
               i=1|
j = 0 ~ N-2       |j=2 -> arr[1], arr[2] = arr[2], arr[1]

            6<8 -> i+=1
             0  1  2 | 3  4  5
             7  3  10| 6  9  8
                  i=2|
j = 0 ~ N-2          |j=3 -> arr[2], arr[3] = arr[3], arr[2]

            9>8 -> 어떤 action도 없음
             0  1  2 | 3  4  5
             7  3  6 |10  9  8
                  i=2|
j = 0 ~ N-2          |   j=4 -> for문 다 돌았기 때문에 arr[i + 1], arr[r] = arr[r], arr[i + 1]
                                                     arr[3], arr[5] = arr[5], arr[3]

            정렬 1차            -> pivot = 3
             0  1  2 | 3  4  5
             7  3  6 | 8  9  10
'''



for t in range(int(input())):
    N = int(input())
    idx = N // 2
    arr = list(map(int, input().split()))
    q_sort(0, N - 1)
    print('#{} {}'.format(t+1, arr[idx]))


