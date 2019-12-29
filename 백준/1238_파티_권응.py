from heapq import heappop, heappush

def go2party(st, ed):
    spendt = [999999999999999999] * (n+1)
    q = []
    heappush(q, [0, st])
    if st == ed:
        return
    while q:
        time, point = heappop(q)
        for nxt_time, nxt in nxt_ls[point]:
            to_time = nxt_time+time
            if spendt[nxt] > to_time:
                spendt[nxt] = to_time
                heappush(q, [to_time, nxt])
    temp = spendt[ed]
    spendt = [999999999999999999] * (n+1)
    heappush(q, [0, ed])
    while q:
        time, point = heappop(q)
        for nxt_time, nxt in nxt_ls[point]:
            to_time = nxt_time+time
            if spendt[nxt] > to_time:
                spendt[nxt] = to_time
                heappush(q,[to_time,nxt])
    spend[st] = temp + spendt[st]


n, m, x = map(int, input().split())
nxt_ls = [[] for i in range(n+1)]

for i in range(m):
    st, ed, t = map(int, input().split())
    nxt_ls[st].append([t, ed])

spend = [0]*(n+1)
for i in range(1, n+1):
    go2party(i, x)
print(max(spend))

