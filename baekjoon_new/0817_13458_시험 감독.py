'''
3
3 4 5
2 2

5
1000000 1000000 1000000 1000000 1000000
5 7

5
10 9 10 9 10
7 20

5
10 9 10 9 10
7 2
'''

N = int(input())
test = list(map(int, input().split()))
B, C = map(int, input().split())

cnt = 0
for person in test:
    cnt += 1
    if person >= B:
        person -= B

        if person % C == 0:
            cnt += person // C
        else:
            cnt += person // C + 1

print(cnt)

