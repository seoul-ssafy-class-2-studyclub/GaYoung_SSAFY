import math
grades = ['A+', 'A0','A-','B+','B0','B-','C+','C0','C-','D0']

T = int(input())
for t in range(1, T + 1):
    students, q_student = map(int,input().split())

    total = []
    for i in range(students):
        scores = list(map(int, input().split()))
        total.append(0.35 * scores[0] + 0.45 * scores[1] + 0.2 * scores[2])
    total_re = sorted(total, reverse = True)
    target_score = total[q_student-1]

    result = total_re.index(target_score) + 1
    how_many = students / 10
    answer = grades[math.ceil(result/how_many - 1)]
    print(f'#{t} {answer}')
    