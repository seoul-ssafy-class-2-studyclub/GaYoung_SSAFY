n = 10
colors = [1,1,2,2,2,3,3,3,2,2]


from itertools import permutations

colors = colors + [0]
check = []
start = 0
for i in range(1, len(colors)):
    if colors[i-1] != colors[i]:
        check.append([colors[i-1], len(colors[start:i])])
        start = i


mymax = 0

length = len(check)
ls = [i for i in range(length)]
results = list(permutations(ls, length))
for result in results:
    check_copy = check[:]
    visit = []
    answer = 0
    while check_copy:
        x = check_copy



