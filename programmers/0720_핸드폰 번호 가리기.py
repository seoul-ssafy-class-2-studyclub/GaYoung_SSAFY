def solution(phone_number):
    num = len(phone_number) - 4

    answer = '*' * num + phone_number[num:]
    # print(answer)
    return answer

print(solution('027778888'))