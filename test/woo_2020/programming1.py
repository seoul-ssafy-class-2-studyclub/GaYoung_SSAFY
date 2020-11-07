def solution(grades, weights, threshold):
    scores = {'A+': 10, 'A0': 9, 'B+': 8, 'B0': 7, 'C+': 6, 'C0': 5, 'D+': 4, 'D0': 3, 'F': 0}

    answer = 0
    for i in range(len(grades)):
        answer += weights[i] * scores[grades[i]]

    answer -= threshold
    return answer