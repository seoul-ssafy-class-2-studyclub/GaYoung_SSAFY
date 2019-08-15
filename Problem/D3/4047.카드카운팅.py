for t in range(int(input())):
    S = D = H = C = 0
    card_list = input()
    card = []
    for i in range(len(card_list) // 3):
        card += [card_list[i * 3 : 3 * (i + 1)]]
        
    if len(card) != len(set(card)):
        result = 'ERROR'
    else:
        for k in range(len(card_list) // 3):
            if card[k][0] == 'S':
                S += 1
            elif card[k][0] == 'D':
                D += 1
            elif card[k][0] == 'H':
                H += 1
            else:
                C += 1

        result = '{} {} {} {}'.format(13 - S, 13 - D, 13 - H, 13 - C)
    
    print('#{} {}'.format(t+1, result))
