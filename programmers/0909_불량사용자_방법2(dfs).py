user_id = ["frodo", "fradi", "crodo", "abc123", "frodoc"]
banned_id = ["fr*d*", "abc1**"]

# user_id = ["frodo", "fradi", "crodo", "abc123", "frodoc"]
# banned_id = ["*rodo", "*rodo", "******"]

# user_id = ["frodo", "fradi", "crodo", "abc123", "frodoc"]
# banned_id = ["fr*d*", "*rodo", "******", "******"]


def correct(user, banned):
    if len(user) != len(banned):  # 글자 수가 맞아야함
        return False
    else:
        for j in range(len(user)):
            if banned[j] == '*':
                continue
            if user[j] != banned[j]:
                return False

    return True

def solution(user_id, banned_id):
    return 0

user_check = [0] * len(user_id)
banned_check = [0] * len(banned_id)
