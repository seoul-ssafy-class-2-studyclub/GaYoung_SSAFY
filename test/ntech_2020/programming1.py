# flowers = [[2, 5], [3, 7], [10, 11]]

flowers = [[3, 4],[4, 5], [6, 7], [8, 10]]

def add(start, end, check):
    for i in range(start, end):
        check[i] += 1

last = 0
for flower in flowers:
    if flower[1] > last:
        last = flower[1]

check = [0] * last

for flower in flowers:
    add(flower[0]-1, flower[1]-1, check)

print(last - check.count(0))
