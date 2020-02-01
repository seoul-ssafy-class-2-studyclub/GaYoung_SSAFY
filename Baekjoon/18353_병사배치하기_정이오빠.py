def search(lo, hi, n):
    if lo == hi:
        return lo
    elif lo + 1 == hi:
        return lo if lis[lo] <= n else hi
    mid = (lo + hi) // 2
    if lis[mid] == n:
        return mid
    elif lis[mid] < n:
        return search(lo, mid, n)
    else:
        return search(mid+1, hi, n)


N = int(input())
soldiers = list(map(int, input().split()))
INF = float('inf')
lis = [INF] * (N+1)
lis[0] = INF
lis[1] = soldiers[0]
max_length = 0
for soldier in soldiers:
    if soldier < lis[max_length]:
        max_length += 1
        lis[max_length] = soldier
    else:
        idx = search(0, max_length, soldier)
        lis[idx] = soldier

print(N-max_length)