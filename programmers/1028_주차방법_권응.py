from collections import deque
# arr = [[1,2], [3,4], [5,6], [-1,7], [8,9], [-1,-1], [-1,-1], [-1,-1], [-1,-1], [-1,-1]]
arr = [[1,2],[3,4],[-1,-1],[-1,-1],[-1,-1]]
def comb(n):
    rs = n*(n-1)
    return rs//2


n = len(arr)
nxt_arr = [-1 for i in range(n)]
cnt_arr = [0]*n
leaf = deque()
for i, item in enumerate(arr):
    l,r = item
    if l>0:
        nxt_arr[l] = i
    if r>0:
        nxt_arr[r] = i
    if i >0:
        leaf.append(i)

while leaf:
    node = leaf.popleft()
    nxt = nxt_arr[node]
    cnt_arr[nxt] += 1
    if nxt_arr[nxt] >= 0:
        leaf.append(nxt)
print(comb(n)- sum(cnt_arr))