from itertools import permutations

N, M = map(int, input().split())
ls = [str(i) for i in range(1, N+1)]
result = list(permutations(ls, M))

# print(result)
for r in result:
    print(' '.join(r))

'''
[1, 2, 3, 4]
[1, 2, 4, 3]
[1, 3, 2, 4]
'''

# result
# def perm()