# def solution(tickets):
#     answer = []
#     return answer

# tickets = [['ICN', 'JFK'], ['HND', 'IAD'], ['JFK', 'HND']]
tickets = [['ICN', 'SFO'], ['ICN', 'ATL'], ['SFO', 'ATL'], ['ATL', 'ICN'], ['ATL','SFO']]

dic = {}
for i in tickets:
    if i[0] not in dic:
        dic[i[0]] = [i[1]]
    else:
        dic[i[0]].append(i[1])

for value in dic.values():
    value.sort()

queue = ['ICN']
ans = []
while len(queue) == 0:
    go = queue[0]

    if go
            ans.append(queue.pop(0))

    res = queue.pop()



