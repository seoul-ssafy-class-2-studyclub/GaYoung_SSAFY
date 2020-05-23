import itertools

def solution(n):
    x = 0
    while True:
        x += 1
        if 3 + 4 * (x - 1) >= n:
            break

    # print(x) -> x = 2
    numb = [3 ** i for i in range(x + 1)]
    check = []
    for i in range(1, len(numb) + 1):
        res = list(itertools.combinations(numb, i))
        check += res
    # print(check)

    sum_ls = []
    for i in range(len(check)):
        sum_ls.append(sum(check[i]))
    sum_ls = sorted(sum_ls)
    # print(sum_ls)
    # print(sum_ls[n - 1])

    return sum_ls[n - 1]

# n = 4
n = 11

x=0
while True:
    x += 1
    if 3 + 4 * (x - 1) >= n:
        break

# print(x) -> x = 2
numb = [3**i for i in range(x+1)]
check = []
for i in range(1, len(numb)+1):
    res = list(itertools.combinations(numb, i))
    check+=res
# print(check)

sum_ls = []
for i in range(len(check)):
    sum_ls.append(sum(check[i]))
sum_ls = sorted(sum_ls)
# print(sum_ls)
print(sum_ls[n-1])