def solution(record):
    answer = []
    users = {}  # {'uid1234':'M', 'uid1234':'P'}
    temp = []  # [['uid1234', '님이 들어왔습니다.' ]] -> 이후에 uid가 최종적으로 결정나면 그 값을 바꿔주기
    for rec in record:
        log = rec.split(' ')

        enter = '님이 들어왔습니다.'
        leave = '님이 나갔습니다.'

        if log[0] == 'Enter':
            users[log[1]] = log[2]
            temp.append([log[1], enter])
            # 여기서 log[1]+enter해버리면 'uid1234님이 들어왔습니다.'처럼 하나의 문장으로 만들어짐(둘 다 str이라서)

        elif log[0] == 'Leave':
            temp.append([log[1], leave])

        elif log[0] == 'Change':
            users[log[1]] = log[2]

    for i in temp:
        answer.append(users[i[0]] + i[1])

    return answer

record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]
