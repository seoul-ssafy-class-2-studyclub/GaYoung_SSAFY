for t in range(10):
    size = int(input())
    board = []   # 보드만들기
    count = 0

    for i in range(size):
        board.append(list(input().split())) # 보드바꾸기? -> 실패 -> N  [0][1][2]..[size]  S 
        board_re = list(map(list, zip(*board)))
    # print(board_re)  # [('1', '0', '0', '0', '0', '0', '0'),,,]으로 나온다

    for j in board_re:
        a = ''.join(j).split('0')
        a_str = ''.join(a)  # str type
        
        count += a_str.count('12')  # str만 가능!
    print('#{0} {1}'.format(t+1, count))

    # 함수 안쓰고 푸는 방법!!!!!!
    # for k in range(len(a_str)-1):
    #     print(k)
    #     if a_str[k] == '1' and a_str[k+1] == '2':
    #         count += 1
    #         print(count)
