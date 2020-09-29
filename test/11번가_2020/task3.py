A = [1, 2, 1]  # [1,2,3], [3,2,1], [1,3,2], [2,3,1] #return 2
# A = [2, 1, 4, 4] # [2, 1, 4, 3],[2, 1, 3, 4] # return 1
# A = [6,2,3,5,6,3]  # [6,2,1,5,4,3] # return 4

def solution(A):
    visit = {}
    max_num = len(A)
    for i in range(max_num):
        visit[i + 1] = 0

    for i in range(len(A)):
        visit[A[i]] += 1

    need = []
    have = []
    for key, val in visit.items():
        if val == 0:
            need.append(key)
        elif val > 1:
            have.append(key)

    cnt = 0
    for i in range(len(need)):
        cnt += abs(need[i] - have[i])

    return cnt


