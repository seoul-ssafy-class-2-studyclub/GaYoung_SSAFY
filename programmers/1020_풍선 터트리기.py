# a = [9,-1,-5]
a = [-16,27,65,-2,58,-92,-71,-68,-61,-33]

'''
1. 리스트의 맨 앞과 맨 뒤 값은 항상 남을 수 있다.
2. 기본적으로 두개의 풍선 중 큰 풍선을 터트려야 한다.
   - 리스트 중간에 있는 풍선은, 자신을 둘러싼 풍선의 최소값보다 작으면 남을 수 있다.
'''
import math

amswer = 0
left, right = math.inf, math.inf
board = [[0] * len(a) for _ in range(2)]

# 왼쪽 기준으로 번호가 작은 풍선을 남기는 경우
for i in range(len(a)):
    if left > a[i]:
        left = a[i]
    board[0][i] = left

# 오른쪽 기준으로 번호가 작은 풍선을 남기는 경우
for i in range(len(a)-1, -1, -1):
    if right > a[i]:
        right = a[i]
    board[1][i] = right

answer = 0
for i in range(len(a)):
    if a[i] <= board[0][i] or a[i] <= board[1][i]:
        answer += 1

print(answer)

'''
[로직]
1. 풍선이 끝까지 남기 위해서는 이 풍선보다 작은 풍선이 없거나, 풍선의 왼쪽 오른쪽에 해당 풍선보다 큰 풍선이 존재해야함.
2. 반대로 생각했을 때 양끝에서 시작했을 때 자기보다 작은 숫자의 풍선이 있다면 해당 풍선은 남을 수 있는 풍선
3. 위와 같이 생각했을 때 양쪽 끝값은 무조건 남길 수 있다. -> left와 right는 자기보다 작은 숫자가 나타날 때 갱신됨
남는 풍선 = left에 갱신된 횟수 + right에 갱신된 횟수 + 양끝값 개수(2) - 1(중복일 경우)
'''
def solution(a):
    ret = 2
    if 0 <= len(a) <= 2:
        return len(a)
    left = a[0]
    right = a[-1]

    for i in range(1, len(a) - 1):
        if left > a[i]:
            left = a[i]
            ret += 1
        if right > a[-1 - i]:
            right = a[-1 - i]
            ret += 1
    if left == right:
        return ret - 1
    else:
        return ret