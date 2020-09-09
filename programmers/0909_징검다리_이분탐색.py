'''
* 처음 문제 접근
 - rocks에서 어떤 값을 빼고 정렬한 후에 거리를 측정하자
 - 분류가 이분탐색인데 어떤 것을 기준으로 하지? -> 기준설정이 어렵군,,,

* 올바른 접근
 - 기준에 맞춰 빼주고, 빼준 갯수가 n개인지 확인
 - 분류가 이분탐색인데 어떤 것을 기준으로 하지? -> 기준설정이 어렵군,,,
'''


'''
[풀이과정]
 - distance 제한사항이 1,000,000,000이다 -> 터지겠다 -> 로그로 가야겠다
 - distance를 기준으로 거리의 최소값이 (start + end) // 2가 될수 있을까?를 탐색하는것
 - log(1000000000) * 50000 으로 빅오를 짤꺼니까 for문을 돌아도 50000이 나온다.
 50000
'''

'''
제한사항을 봤을 때 for문 2번 돌리면 안되는 애들을 log(N)으로 바꿔야하고 그러면 이분탐색밖에 없다.
그거를 기준으로 하면
'''

distance = 25
rocks = [2, 14, 11, 21, 17]
n = 2


def solution(distance, rocks, n):
    rocks.sort()
    rocks.append(distance)
    start, end = 0, distance
    answer = 0  # 각 지점 사이 거리의 최소값 중에 가장 큰 값이므로 answer = mymax인 것이다.

    while start <= end:
        before_rock = 0  # 이전 돌
        mymin = 1000000001  # 돌 거리의 최소값을 구하기 위함
        removed_rocks = 0  # n과 비교할 값

        mid = (start + end) // 2  # 바위 사이의 최소 거리???????????????????????????

        for i in range(len(rocks)):
            if rocks[i] - before_rock < mid:
                removed_rocks += 1
            else:
                mymin = min(mymin, rocks[i] - before_rock)
                before_rock = rocks[i]   # 현재 rock을 before로 바꿔주기

        # 제거한 돌 갯수가 기준보다 많다 = 바위 제거를 줄여야 한다.
        # 바위 사이 최소거리의 기준을 낮춰야한다.
        if removed_rocks > n:   # -> 통과할 수 있는 애들찾기
            '''
            removed_rocks이 많으면 우리가 더 많이 제거하게 된 것 
            우리는 최소값으로 removed_rocks을 고른것이니까
            우리는 removed_rocks을 줄여야하니까 mid를 줄여야함 -> 끝에값을 줄여줌
            우리가 설정한 mid가 줄어드니까 removed_rocks가 줄어든다.
            '''
            end = mid - 1

        # 제거한 돌 개수가 기준보다 적다 = 바위 제거를 더 해야한다 = 바위 사이 최소거리를 높여야한다.
        else:
            answer = mymin  # 거리의 최소값 -> 일단은 바꿔놓고
            start = mid  # 진짜 최소값인지아닌지 확인하려고 start를 바꿔준다.

    return answer

print(solution(distance, rocks, n))
