import math
grades = ['A+', 'A0','A-','B+','B0','B-','C+','C0','C-','D0'] 
 
T = int(input())
for t in range(1, T + 1): 
    students, q_student = map(int,input().split()) 
 
    total = []
# goal_student = s_scores, score = total
    for i in range(students): # 0, 1, 2
        scores = list(map(int, input().split())) 
        total.append(0.35 * scores[0] + 0.45 * scores[1] + 0.2 * scores[2])
    # print(total)  # [74.6, 92.55000000000001, 88.8, 99.45, 72.35,,,]
    total_re = sorted(total, reverse = True)
    # print(total)
    target_score = total[q_student-1]
    # print(target_score)  # 96.25
 
    result = total_re.index(target_score) + 1  # 1
    # print(result)
    how_many = students / 10  # ex. student=10이면 1명씩 줄 수 있음
    answer = grades[math.ceil(result/how_many - 1)]
    print(f'#{t} {answer}')
