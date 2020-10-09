# depar = "SEOUL"
# hub = "DAEGU"
# dest = "YEOSU"
# roads = [["ULSAN","BUSAN"],["DAEJEON","ULSAN"],["DAEJEON","GWANGJU"],["SEOUL","DAEJEON"],["SEOUL","ULSAN"],["DAEJEON","DAEGU"],["GWANGJU","BUSAN"],["DAEGU","GWANGJU"],["DAEGU","BUSAN"],["ULSAN","DAEGU"],["GWANGJU","YEOSU"],["BUSAN","YEOSU"]]

depar = "ULSAN"
hub = "SEOUL"
dest = "BUSAN"
roads = [["SEOUL","DAEJEON"],["ULSAN","BUSAN"],["DAEJEON","ULSAN"],["DAEJEON","GWANGJU"],["SEOUL","ULSAN"],["DAEJEON","BUSAN"],["GWANGJU","BUSAN"]]

from collections import deque

city = {}
for start, end in roads:
    if start not in city:
        city[start] = [end]
    else:
        city[start].append(end)


q = deque([[depar]])
cnt = 0
while q:
    x = q.popleft()
    st = x[-1]

    if st == dest:
        if hub in x:
            cnt += 1

    if st != dest:
        for i in city[st]:  # case2에서 서울->대전->울산 한번에 넣어지므로 q에 넣을때 같이 넣어야함
            q.append(x+[i])

cnt = cnt % 10007
print(cnt)
'''
SEOUL → DAEJEON → DAEGU → BUSAN → YEOSU
SEOUL → DAEJEON → DAEGU → GWANGJU → YEOSU
SEOUL → DAEJEON → DAEGU → GWANGJU → BUSAN → YEOSU
SEOUL → DAEJEON → ULSAN → DAEGU → BUSAN → YEOSU
SEOUL → DAEJEON → ULSAN → DAEGU → GWANGJU → YEOSU
SEOUL → DAEJEON → ULSAN → DAEGU → GWANGJU → BUSAN → YEOSU
SEOUL → ULSAN → DAEGU → BUSAN → YEOSU
SEOUL → ULSAN → DAEGU → GWANGJU → YEOSU
SEOUL → ULSAN → DAEGU → GWANGJU → BUSAN → YEOSU
'''
# {'ULSAN': ['BUSAN', 'DAEGU'], 'DAEJEON': ['ULSAN', 'GWANGJU', 'DAEGU'], 'SEOUL': ['DAEJEON', 'ULSAN'], 'GWANGJU': ['BUSAN', 'YEOSU'], 'DAEGU': ['GWANGJU', 'BUSAN'], 'BUSAN': ['YEOSU']}
# deque([['SEOUL', 'DAEJEON', 'GWANGJU', 'YEOSU'],
#        ['SEOUL', 'DAEJEON', 'DAEGU', 'GWANGJU'],
#        ['SEOUL', 'DAEJEON', 'DAEGU', 'BUSAN'],
#        ['SEOUL', 'ULSAN', 'BUSAN', 'YEOSU'],
#        ['SEOUL', 'ULSAN', 'DAEGU', 'GWANGJU'],
#        ['SEOUL', 'ULSAN', 'DAEGU', 'BUSAN'],
#        ['SEOUL', 'DAEJEON', 'ULSAN', 'BUSAN', 'YEOSU'],
#        ['SEOUL', 'DAEJEON', 'ULSAN', 'DAEGU', 'GWANGJU'],
#        ['SEOUL', 'DAEJEON', 'ULSAN', 'DAEGU', 'BUSAN'],
#        ['SEOUL', 'DAEJEON', 'GWANGJU', 'BUSAN', 'YEOSU']])
