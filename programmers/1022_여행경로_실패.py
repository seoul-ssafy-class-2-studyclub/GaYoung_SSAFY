def solution(tickets):
    answer = []
    return answer

tickets = [['ICN', 'SFO'], ['ICN', 'ATL'], ['SFO', 'ATL'], ['ATL', 'ICN'], ['ATL','SFO']]
# tickets = [['ICN', 'JFK'], ['HND', 'IAD'], ['JFK', 'HND']]

check = {}
for start, end in tickets:
    if start not in check:
        check[start] = [end]
    else:
        check[start].append(end)

    for value in check.values():
        value.sort()

# print(check)
{'ICN': ['ATL', 'SFO'], 'SFO': ['ATL'], 'ATL': ['ICN', 'SFO']}
['SFO', 'ATL', 'SFO', 'ICN', 'ATL', 'ICN']


# answer = ['ICN']
# go = []
# while answer:
#     temp = answer[-1]


