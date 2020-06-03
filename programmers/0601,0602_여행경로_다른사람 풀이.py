# def solution(tickets):
#
#
#     return ans


# tickets = [['ICN', 'JFK'], ['HND', 'IAD'], ['JFK', 'HND']]
# tickets = [['ICN', 'SFO'], ['ICN', 'ATL'], ['SFO', 'ATL'], ['ATL', 'ICN'], ['ATL','SFO']]
# tickets = [['ICN', 'COO'], ['COO', 'ICN'],['ICN', 'COO']]
tickets = [['ICN','BOO'], ['ICN', 'COO'], ['COO', 'DOO'], ['DOO', 'COO'],
           ['BOO', 'DOO'], ['DOO', 'BOO'], ['BOO', 'ICN'], ['COO', 'BOO'],
           ['BOO', 'COO'], ['COO', 'ICN'], ['ICN', 'DOO']]

def solution(tickets):
    routes = {}
    for t in tickets:
        routes[t[0]] = routes.get(t[0], []) + [t[1]]
    for r in routes:
        routes[r].sort(reverse=True)

    stack = ["ICN"]
    path = []
    while len(stack) > 0:
        # print('stack')
        # print(stack)
        # print('path')
        # print(path)

        top = stack[-1]
        if top not in routes or len(routes[top]) == 0:
            path.append(stack.pop())
        else:
            stack.append(routes[top][-1])
            # print('routes[top][-1]')
            # print(routes[top][-1])
            routes[top] = routes[top][:-1]
            # print('routes[top]')
            # print(routes[top])
            # print('----------------------------------')

    return path[::-1]
print('--------------------------------------------------')
print(solution(tickets))
# dic = {}
# for i in tickets:
#     if i[0] not in dic:
#         dic[i[0]] = [i[1]]
#     else:
#         dic[i[0]].append(i[1])
#
# for value in dic.values():
#     value.sort(reverse=True)
#
# print(dic)
# print(dic['ICN'][:-1])

# go = ["ICN"]
# ans = []
#
# while go:
#     first = go[-1]
#
#     if first not in dic or len(dic[first]) == 0:
#         ans.append(go.pop(0))
#
#     else:
#         go.append(dic[first][0])
#
#
# print('go')
# print(go)
# print('ans')
# print(ans)
