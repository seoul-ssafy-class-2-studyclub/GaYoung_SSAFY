N = int(input())
l_list = []
h_list = []
for n in range(N):
    L, H = list(map(int, input().split()))
    l_list.append(L)
    h_list.append(H)
print(l_list)
print(h_list)
