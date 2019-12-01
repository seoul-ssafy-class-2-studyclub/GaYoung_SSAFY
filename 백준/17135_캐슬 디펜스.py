def perm(x,ls=[],st=0):
   if len(ls) == 3:
       su_set.append(ls)
       return 0
   for i in range(st,x):
       if i not in ls:
           perm(x,ls+[i],i+1)
def start():
   global n, d, cnt
   shoot = []
   for r1,c1 in ranger:
       mn = 1000000
       target=[]
       for r2,c2 in enermy:
           dt = abs(r1-r2)+abs(c1-c2)
           if dt <= d:
               if dt < mn:
                   target=[r2,c2]
                   mn = dt
               elif dt == mn:
                   if target:
                       if c2 < target[1]:
                           target=[r2,c2]
       if target not in shoot:
           shoot.append(target)
   for i in range(len(enermy)):
       x,y = enermy.pop(0)
       if [x,y] not in shoot:
           if x != n-1:
               enermy.append([x+1, y])
       else:
           cnt +=1
n, m, d = map(int, input().split())
su_set=[]
enermy_origin = []
for i in range(n):
   a = list(map(int, input().split()))
   for j in range(m):
       if a[j] == 1:
           enermy_origin.append([i,j])
perm(m)

rs_set = []
for j in su_set:
   enermy = [i[:] for i in enermy_origin]
   ranger = []
   len(enermy)
   cnt = 0
   for k in j:
       ranger.append([n,k])
   for i in range(n):
       if enermy:
           start()
   rs_set.append(cnt)
print(max(rs_set))