N, M = map(int, input().split())
cnt = 0

truth = set()
knowing = list(map(int, input().split()))[1:]
know = [0] * (N + 1)


# if not truth_people:
#     print(M)
# else:
#     for m in range(M):
#         party_attendance = list(map(int, input().split()))[1:]
#         for t in truth_people:
#             if t in party_attendance:
#                 know[t] = 1
