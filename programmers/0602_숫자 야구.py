import itertools

def check(ls, number, ss, bb):
    strike = 0
    for l in range(len(ls)):
        if ls[l] == number[l]:
            strike += 1

    if ss != strike:
        return False

    ball = len(set(ls) & set(number)) - strike
    if bb != ball:
        return False

    return True

# print(check([int(i) for i in str(asdf[0])], number, asdf[1], asdf[2]))



def solution(baseball):
    all_ball = list(itertools.permutations([1, 2, 3, 4, 5, 6, 7, 8, 9], 3))

    for base in baseball:
        for ball in all_ball:
            # print(check(lst, ball, base[1], base[2]))
            if not check([int(i) for i in str(base[0])], ball, base[1], base[2]):
                all_ball.remove(ball)

    for base in baseball:
        # all_ball[:] 과 all_ball의 차이
        # all_ball: 계속 맨처음 생성된 all_ball기준으로 remove
        # all_ball[:]: remove가 진행된 all_ball기준으로 계속 remove
        for ball in all_ball[:]:
            if not check([int(i) for i in str(base[0])], ball, base[1], base[2]):
                all_ball.remove(ball)
                # print(all_ball)

    return len(all_ball)


all_ball = list(itertools.permutations([1,2,3,4,5,6,7,8,9], 3))
baseball = [[123, 1, 1], [356, 1, 0], [327, 2, 0], [489, 0, 1]]



for ball in all_ball:
    all_ball.remove(ball)
    print('all_ball1')
    print(all_ball)
print('---------------------------------------------------')

for ball in all_ball[:]:
    all_ball.remove(ball)
    print('all_ball2')
    print(all_ball)

