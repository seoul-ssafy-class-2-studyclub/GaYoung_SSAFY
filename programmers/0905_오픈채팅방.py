def solution(record):
    user = {}
    result = []
    for r in record:
        rec = r.split(' ')
        if rec[0] == 'Enter':
            user[rec[1]] = rec[2]
            result.append((rec[1], '님이 들어왔습니다.'))
        elif rec[0] == 'Leave':
            result.append((rec[1], '님이 나갔습니다.'))
        else:
            user[rec[1]] = rec[2]

    answer = []
    for i in result:
        answer.append(user[i[0]] + i[1])

    return answer

record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]

