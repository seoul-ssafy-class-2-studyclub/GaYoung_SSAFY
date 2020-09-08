def solution(name):
    cnt = 0
    move = 0
    a = ord('A')
    z = ord('Z')
    name = list(name)

    if name == ['A'] * len(name):
        return 0

    while True:
        if name[move] != 'A':
            if (ord(name[move]) - a) <= 13:
                plus = ord(name[move]) - a
            else:
                plus = (z - ord(name[move]) + 1)
            cnt += plus
            # print(cnt)

        name[move] = 'A'
        if name == ['A'] * len(name):
            break

        name[0] = 'A'
        right, left = 1, 1
        for i in range(1, len(name)):
            if name[move + i] == 'A':
                right += 1
            else:
                break

        for i in range(1, len(name)):
            if name[move - i] == 'A':
                left += 1
            else:
                break

        if right <= left:
            cnt += right
            move += right

        else:
            cnt += left
            move -= left


    return cnt