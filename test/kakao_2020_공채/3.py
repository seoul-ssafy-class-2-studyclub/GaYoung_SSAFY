def solution(info, query):
    answer = []
    return answer


info = ["java backend junior pizza 150",
        "python frontend senior chicken 210",
        "python frontend senior chicken 150",
        "cpp backend senior pizza 260",
        "java backend junior chicken 80",
        "python backend senior chicken 50"]
query = ["java and backend and junior and pizza 100",
         "python and frontend and senior and chicken 200",
         "cpp and - and senior and pizza 250",
         "- and backend and senior and - 150",
         "- and - and - and chicken 100","- and - and - and - 150"]

import collections
import json

def tree():
    return collections.defaultdict(tree)

data = tree()
for i in info:
    lang, job, age, food, score = i.split()
    score = int(score)
    # print(lang, job, age, food, score)
    data[lang][job][age][food] = score
    # data[lang]
# print(json.dumps(data))
print(type(data['java']['backend']['junior']['pizza']))
'''
{"java":
     {"backend":
          {"junior":
               {"pizza": "150",
                "chicken": "80"}}},
 "python":
     {"frontend":
          {"senior":
               {"chicken": "150"}},
      "backend":
          {"senior":
               {"chicken": "50"}}},
 "cpp":
     {"backend":
          {"senior":
               {"pizza": "260"}}}
 }
'''

first = ['java', 'python', 'cpp']
second = ['backend', 'frontend']
third = ['junior', 'senior']
forth = ['chicken', 'pizza']

answer = []
for i in query:
    lang, job, age, food = i.split(' and ')
    food, score = food.split()
    score = int(score)
    cnt = 0

    if lang != '-':
        if job != '-':
            if age != '-':
                if food != '-':
                    # print(type(score), type(data[lang][job][age][food]))
                    if score <= data[lang][job][age][food]:
                        cnt += 1
            #     else:
            #         for ff in forth:
            #             if score <= data[lang][job][age][ff]:
            #                 cnt += 1
            # else:  # if age == '-':
            #     for t in third:
            #         if food != '-':
            #             if score <= data[lang][job][t][food]:
            #                 cnt += 1
            #         else:
            #             for ff in forth:
            #                 if score <= data[lang][job][t][ff]:
            #                     cnt += 1
        # else:  # job == '-'
        #     for s in second:
        #         if age != '-':
        #             if food != '-':
        #                 print('aaaaaaa')
        #                 print(data[lang][s][age][food])
    #                     if score <= data[lang][s][age][food]:
    #                         cnt += 1
    #                 else:
    #                     for ff in forth:
    #                         if score <= data[lang][s][age][ff]:
    #                             cnt += 1
    #             else:
    #                 for t in third:
    #                     if food != '-':
    #                         if score <= data[lang][s][t][food]:
    #                             cnt += 1
    #                     else:
    #                         for ff in forth:
    #                             if score <= data[lang][s][t][ff]:
    #                                 cnt += 1
    #
    # else:
    #     for f in first:
    #         if job != '-':
    #             if age != '-':
    #                 if food != '-':
    #                     if score <= data[f][job][age][food]:
    #                         cnt += 1
    #                 else:
    #                     for ff in forth:
    #                         if score <= data[f][job][age][ff]:
    #                             cnt += 1
    #             else:  # if age == '-':
    #                 for t in third:
    #                     if food != '-':
    #                         if score <= data[f][job][t][food]:
    #                             cnt += 1
    #                     else:
    #                         for ff in forth:
    #                             if score <= data[f][job][t][ff]:
    #                                 cnt += 1
    #         else:  # job == '-'
    #             for s in second:
    #                 if age != '-':
    #                     if food != '-':
    #                         if score <= data[f][s][age][food]:
    #                             cnt += 1
    #                     else:
    #                         for ff in forth:
    #                             if score <= data[f][s][age][ff]:
    #                                 cnt += 1
    #                 else:
    #                     for t in third:
    #                         if food != '-':
    #                             if score <= data[f][s][t][food]:
    #                                 cnt += 1
    #                         else:
    #                             for ff in forth:
    #                                 if score <= data[f][s][t][ff]:
    #                                     cnt += 1

    answer.append(cnt)


print(answer)

# info = ["java backend junior pizza 150",
#         "python frontend senior chicken 210",
#         "python frontend senior chicken 150",
#         "cpp backend senior pizza 260",
#         "java backend junior chicken 80",
#         "python backend senior chicken 50"]
# query = ["java and backend and junior and pizza 100",
#          "python and frontend and senior and chicken 200",
#          "cpp and - and senior and pizza 250",
#          "- and backend and senior and - 150",
#          "- and - and - and chicken 100","- and - and - and - 150"]
#
# data = []
# for i in info:
#     data.append(i.split())
# # print(data)
# # [['java', 'backend', 'junior', 'pizza', '150'],
# #  ['python', 'frontend', 'senior', 'chicken', '210'],
# #  ['python', 'frontend', 'senior', 'chicken', '150'],
# #  ['cpp', 'backend', 'senior', 'pizza', '260'],
# #  ['java', 'backend', 'junior', 'chicken', '80'],
# #  ['python', 'backend', 'senior', 'chicken', '50']]
#
#
# # q_data = []
# # for i in query:
# #     for j in range(len(i)):
#
#
#     # q_data.append(qq)
# # print(q_data)
#
