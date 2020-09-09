# 시간초과
def solution_not_pass(k, room_number):
    check = [0] * (k + 1)
    answer = []
    for i in range(len(room_number)):
        if check[room_number[i]] == 0:
            check[room_number[i]] = 1
            answer.append(room_number[i])
        else:
            idx = room_number[i]
            while True:
                if check[idx] == 0:
                    break
                else:
                    idx += 1

            check[idx] = 1
            answer.append(idx)

    return answer

k = 10
room_number = [1,3,4,1,3,1]

def solution(k, room_number):
    check = {}
    answer = []
    for room in room_number:
        reservation = room
        visit = [reservation]
        while reservation in check:
            reservation = check[reservation]
            visit.append(reservation)

        answer.append(reservation)
        for i in visit:
            check[i] = reservation + 1

        # print(answer)
    return answer



