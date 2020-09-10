# 단, 다음으로 밟을 수 있는 디딤돌이 여러 개인 경우 무조건 가장 가까운 디딤돌로만 건너뛸 수 있습니다.

def solution(stones, k):
    answer = 0
    left, right = 0, max(stones)
    while left <= right:  # [2, 4, 5, 3, 2, 1, 4, 2, 5, 1]
        mid = (left + right) // 2  # 니니즈 친구들의 수
        cnt = 0  # 돌을 밟았다는 것을 의미
        for stone in stones:
            if stone < mid:  # 만약에 해당 돌이 니니즈보다 작거나 같으면 니니즈가 돌을 건널 수 없다.
                print('No : 니니즈 다리건널 수 없음')
                cnt += 1  # cnt는 건널 수 없는 돌의 갯수를 세는 것
                if cnt >= k:  # 만약에 연속으로 0이 k번 이상 나타나면 니니즈가 지나갈 수 없다 -> 범위 줄여야함
                              # 지금까지의 범위는 : left~right
                    right = mid - 1  # 더 작은 구간에서 찾아야한다.
                    '''
                    우리는 범위를 줄이는게 right는 최대값 -> 이 최대값을 줄여야한다.
                    ex. 0~10사이에 값을하나 정해보라. 그러면 우리는 5보다 크가 작냐? 확인하는거
                    '''
                    break

            else:
                print('Yes : 니니즈 다리건널 수 있음')
                cnt = 0  # 돌을 밟았다는 것을 의미

        else:  # 돌을 다 지나갈 수 있었다는 의미
            answer = mid
            # print(answer)
            left = mid + 1

    # print(answer)
    return answer

stones = [2, 4, 5, 3, 2, 1, 4, 2, 5, 1]
k = 3

'''
진행과정
1. left, right = 0, 5 -> mid = 2
2. for stone in stones:
     -> 2,4,5,3,2->cnt=0에서 cnt=0으로 갱신, 1->cnt=1에서 stone=4가 되면서 cnt=0으로 갱신
        2,5->cnt=0에서 cnt=0으로 갱신, 1->cnt=1에서 for문이 끝남
3. answer = mid = 2, left = 3으로 갱신
-------------------------------------------------------------------------------------
4. left, right = 3, 5 -> mid = 4
5. for stone in stones:
     -> 2->cnt=1에서 stone=4가 되면서 cnt=0으로 갱신, 4,5->cnt=0에서 cnt=0으로 갱신, 
        3,2,1->cnt=3이 되기때문에 right=3으로 갱신되면서 break에 걸리고 for문이 끝난다.
-------------------------------------------------------------------------------------
6. left, right = 3, 3 -> mid = 3
7. for stone in stones:
     -> 2->cnt=1에서 stone=4가 되면서 cnt=0으로 갱신, 4,5,3->cnt=0에서 cnt=0으로 갱신, 
        2,1->cnt=2가 되고 4에서 cnt=0으로 갱신,2->cnt=1에서 stone=5가 되면서 cnt=0으로 갱신,
        1->cnt=1에서 for문이 끝남
8. answer = mid = 3, left = 4으로 갱신
-------------------------------------------------------------------------------------
9. left, right = 4, 3 -> while문에 들어갈 수 없어서 기존 answer값이 정답
'''

print(solution(stones, k))
