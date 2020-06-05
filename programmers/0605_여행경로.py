# tickets = [['ICN', 'JFK'], ['HND', 'IAD'], ['JFK', 'HND']]
tickets = [['ICN', 'SFO'], ['ICN', 'ATL'], ['SFO', 'ATL'], ['ATL', 'ICN'], ['ATL','SFO']]
# tickets = [['ICN', 'COO'], ['COO', 'ICN'],['ICN', 'COO']]
# tickets = [['ICN', 'BOO'], ['ICN', 'COO'], ['COO', 'DOO'], ['DOO', 'COO'],
#            ['BOO', 'DOO'], ['DOO', 'BOO'], ['BOO', 'ICN'], ['COO', 'BOO']]

def solution(tickets):
    dic = {}
    for i in tickets:
        if i[0] not in dic:
            dic[i[0]] = [i[1]]
        else:
            dic[i[0]].append(i[1])

    for value in dic.values():
        value.sort()

    go = ["ICN"]
    ans = []
    while go:
        first = go[-1]

        # 갈 수 있는 애들은 go에 넣는다
        # 갈 수 없는 애들은 큰 값부터 ans에 넣기 -> 이렇게 되면 go에서 더이상 못가기 전까지 기록이 됨(흔적 남기기 가능)
        if first not in dic or len(dic[first]) == 0:
            ans.append(go.pop())
        else:
            go.append(dic[first].pop())

    # print(ans[::-1])
    return ans[::-1]