from collections import deque

def combi(depth,idx, d_cnt, my_lis):
    global total_cnt
    if d_cnt > 3:
        return
    if depth == 7:
        total_cnt += check(my_lis)
        return
    for j in range(idx, 25):
        if not combi_visited[j]:
            combi_visited[j] = 1
            combi(depth+1, j+1,d_cnt+lis[j], my_lis+[j])
            combi_visited[j] = 0



di = [0,0,-1,1]
dj = [-1,1,0,0]
def check(my_combi):

    visisted = [0] * 7
    visisted[0] = 1
    cnt = 1
    q = deque([(my_combi[0]//5, my_combi[0]%5)])
    while q:
        a = q.popleft()
        x,y = a[0], a[1]
        for k in range(4):
            newX,newY = x+di[k], y+dj[k]
            for j in range(7):
                if visisted[j]:
                    continue
                xx,yy  =  my_combi[j] // 5,my_combi[j] % 5
                if xx == newX and yy == newY:
                    q.append((xx, yy))
                    visisted[j] = 1
                    cnt+=1
    if cnt == 7:
        return 1
    else:
        return 0
lis = []
for i in range(5):
    temp = list(map(lambda x:1 if x == 'Y' else 0, list(input())))
    lis.extend(temp)

# total_cnt = 0
# combi_visited = [0] * 25
# combi(0,0,0, [])
# print(total_cnt)