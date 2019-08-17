def change(switch):
    switch = 0 if switch == 1 else 1
    return switch

def man(multiple):
    for i in range(multiple - 1, N, multiple):
        switch[i] = change(switch[i])
    return switch

def woman(multiple):
    switch[multiple - 1] = change(switch[multiple - 1])
    k = 1
    while multiple - k - 1 >= 0 and multiple + k <= N and switch[multiple - k - 1] == switch[multiple + k - 1]:
        switch[multiple - k - 1] = change(switch[multiple - k - 1])
        switch[multiple + k - 1] = change(switch[multiple + k - 1])
        k += 1

N = int(input())
switch = list(map(int, input().split()))
times = int(input())
for t in range(times):
    person, multiple = map(int, input().split())
    if person == 1:
        man(multiple)
    else:
        woman(multiple)

for s in range(len(switch)):
    print(switch[s], end=' ')
    if (s + 1) % 20 == 0:
        print('')

