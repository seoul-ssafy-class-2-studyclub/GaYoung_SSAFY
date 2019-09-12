N = 35
number = ['3', '6', '9']

result = []
for n in range(1, N + 1):
    cnt = 0
    for i in str(n):
        if i in number:
            cnt += 1

    if cnt > 0:
        result.append('-' * cnt)
    else:
        result.append(n)

for r in result:
    print(r, end=' ')