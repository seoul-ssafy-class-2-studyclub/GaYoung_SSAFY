T = int(input())

for t in T:
    N = int(input())
    a = b = c = d = e = 0
    while i != 1:
        if N % 2 == 0:
            a += 1
        if N % 3 == 0:
            b += 1
        if N % 5 == 0:
            c += 1
        if N % 7 == 0:
            d += 1
        if N % 11 == 0:
            e += 1
print(f'#{t} {a} {b} {c} {d} {e}')

# 논리
# N=2^a * 3^b * 5^c * 7^d * 11^e이니까 N이 2,3,5,7,11로 나뉠때마다 a,b,c,d,e를 1씩 더하면 됨.
# 몫 개수만큼 더하면 됨
# 이때 나누는 수가 1이 아니어야한다. -> 나누는 수가 1이 안될때까지 돌리기

# 소인수
for T in range(int(input())):
    c = []
    x = int(input())
    d = 2
    while d <= x:
        if x % d == 0:
            c.append(d)
            x = x / d
        else:
            d = d + 1          
    print(f'#{T+1} {c.count(2)} {c.count(3)} {c.count(5)} {c.count(7)} {c.count(11)}')



T = int(input())

for i in range(T):
    # 기본설정
    num = int(input())
    dem = [2, 3, 5, 7, 11]
    dem_in = [0, 0, 0, 0, 0]
    
    #소인수분해하기
    for de in range(len(dem)): #각각의 소수에 대하여
        while num % (dem[de]**(dem_in[de]+1)) == 0: #승수를 높혀가며 나눠보기
            dem_in[de] += 1


    print(f'#{i+1} ', end = '')
    for k in range(len(dem)):
        print(f'{dem_in[k]}', end=' ')
    print('')