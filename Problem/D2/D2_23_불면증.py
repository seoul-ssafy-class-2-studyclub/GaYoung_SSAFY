T = int(input())
for t in range(1, T + 1):
    N = int(input())  # 1259
    i = 1
    N_set = set(str(N))
    while len(N_set) < 10:
        N_set.update(str(i*N))
        i += 1
    print(f'#{t} {(i-1)*N}')
    