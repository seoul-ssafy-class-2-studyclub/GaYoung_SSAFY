for t in range(int(input())):
    N, M = map(int, input().split())
    A = [input() for n in range(N)]
    B = [input() for m in range(M)]
    result = [a for a in A if a in B]
    print('#%d %d' % (t+1, len(result)))
