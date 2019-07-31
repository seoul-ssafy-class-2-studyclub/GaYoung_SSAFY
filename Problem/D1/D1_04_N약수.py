n = int(input())
a=[]

if 1 <= n <= 1000:
    for i in range(1, n + 1):
        if n % i == 0 :
            a += [str(i)]

print(' '.join(a))