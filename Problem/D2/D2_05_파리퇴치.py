T = int(input())

for t in range(1, T + 1):
    # 보드만들기
    n, k = list(map(int, input().split()))  # 5(=n=보드크기) 2(=k=파리채크기) 
    board = []
    for i in range(n):
        board.append(list(map(int, input().split()))) # board라는 list에 넣기

    total = []
    for i in range(n - k + 1):  # 파리채가 가능한 부분 5 2 -> 4, 6 3 -> 4  n-k+1     
        for j in range(n - k + 1):  # i:0 1 2 3  j:0 1 2 3
            pari = []  # 파리 잡을 list
            for row_b in range(k): # 파리채 크기 2x2인 경우   row_b:0 1  col_b:0 1
                for col_b in range(k):
                    pari.append(board[i + row_b][j + col_b])
            # print(pari)   # for i,j가 row_b, col_b를 돌리기 위한것이므로 row_b, col_b에 맞게 print하면 [23, 2, 7, 3]식으로 16개 나옴  # 만약에 for col_b 에 맞게 print하면 [23, 2] [23, 2, 7, 3] 이렇게 나옴
            total += [pari]  # total이라는 전체 리스트에 pari넣고 그 중 합의 max구하려함

                        

    # 파리 list를 total에 집어넣어서 각각 파리리스트의 합을 구해 max
    max_list = []
    for p in range(len(total)):
        max_list += [sum(total[p])]
    print(f'#{t} {max(max_list)}')