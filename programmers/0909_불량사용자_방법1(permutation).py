# user_id = ["frodo", "fradi", "crodo", "abc123", "frodoc"]
# banned_id = ["fr*d*", "abc1**"]

# user_id = ["frodo", "fradi", "crodo", "abc123", "frodoc"]
# banned_id = ["*rodo", "*rodo", "******"]

user_id = ["frodo", "fradi", "crodo", "abc123", "frodoc"]
banned_id = ["fr*d*", "*rodo", "******", "******"]

'''
방법1 : permutation해서 하나씩확인하면서 중복된 것 제거
방법2 : visit돌면서 확인하기
'''

# 방법1
from itertools import permutations

def correct(user_ls, banned_ls):
    for i in range(len(user_ls)):
        if len(user_ls[i]) != len(banned_ls[i]):  # 글자 수가 맞아야함
            return False
        else:
            for j in range(len(user_ls[i])):
                # if user_ls[i][j] != banned_ls[i][j]:이거보다 위에 해야 f랑 *랑 비교했을 때 return False에 걸리지 않는다.
                if banned_ls[i][j] == '*':
                    continue
                if user_ls[i][j] != banned_ls[i][j]:
                    return False

    return True

def solution(user_id, banned_id):
    len_ban = len(banned_id)
    perm = list(permutations(user_id, len_ban))

    answer = []
    for i in perm:  # i = ("frodo", "fradi")
        if correct(i, banned_id):
            if set(i) not in answer:
                answer.append(set(i))

    # print(len(answer))
    return len(answer)
