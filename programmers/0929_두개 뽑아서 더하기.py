def solution(numbers):

    answer = []
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            num = numbers[i] + numbers[j]
            if num not in answer:
                answer.append(num)

    answer = sorted(answer)

    return answer