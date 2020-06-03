def solution(name):
    cnt = 0
    move = 0
    a = ord('A')
    z = ord('Z')
    name = list(name)

    if name == ['A'] * len(name):
        return 0

    while True:
        right, left = 1, 1
        for n in range(len(name)):
            if name[n] != 'A':
                if (ord(name[n]) - a) <= 13:
                    plus = ord(name[n]) - a
                else:
                    plus = (z - ord(name[n]) + 1)
                cnt += plus
        # print(cnt)
        # print('-------------------')
        name[move] = 'A'

        # 오른쪽으로 가는 경우
        for i in range(1, len(name)):
            if name[move + i] != 'A':
                right += i-1
            else:
                break
        print('right')
        print(right)

        # 왼쪽으로 가는 경우
        for i in range(1, len(name)):
            if name[move - i] != 'A':
                left += i-1
            else:
                break
        print('left')
        print(left)

        if right <= left:
            cnt += right
            move += right

        else:
            cnt += left
            move -= left

    return cnt



# name = 'JEROEN'
# name = 'JAN'
name = 'ZZAAAAAZ'


print(solution(name))

