from itertools import permutations

def check(user, banned_id):  # result중 하나
    for i in range(len(user)):
        if len(user[i]) != len(banned_id[i]):
            return False
        
        else:
            for j in range(len(user[i])):
                if banned_id[i][j] == '*':
                    continue
                if user[i][j] != banned_id[i][j]:
                    return False
                
    
    return True

# user_id = ["frodo", "fradi", "crodo", "abc123", "frodoc"]
# banned_id = ["fr*d*", "abc1**"]

# user_id = ["frodo", "fradi", "crodo", "abc123", "frodoc"]
# banned_id = ["*rodo", "*rodo", "******"]

user_id = ["frodo", "fradi", "crodo", "abc123", "frodoc"]
banned_id = ["fr*d*", "*rodo", "******", "******"]

def solution(user_id, banned_id):
    len_ban = len(banned_id)
    result = list(permutations(user_id, len(banned_id)))

    answer = []
    for i in result:  # i = ("frodo", "fradi")
        if check(i, banned_id):
            if set(i) not in answer:
                answer.append(set(i))

    # print(len(answer))
    return len(answer)


