def solution(n, lost, reserve):

    # 여벌체육복 가지고온 학생도 도난 가능 -> 그러면 lost, reverse에서 다 제거해야함
    for l in lost[:]:
        if l in reserve:
            lost.remove(l)
            reserve.remove(l)

    for rev in reserve:
        if (rev - 1) in lost:
            lost.remove(rev - 1)
        elif (rev + 1) in lost:
            lost.remove(rev + 1)

    ans = n - len(lost)
    # print(ans)

    return ans

# n = 5
# lost = [2, 4]
# reserve = [1, 3, 5]

# n = 5
# lost = [2, 4]
# reserve = [3]

# n = 3
# lost = [3]
# reserve = [1]

# n = 10
# lost = [2, 3, 4, 8, 10]
# reserve = [1, 3, 6, 9]

n = 5
lost = [1, 2, 3]
reserve = [1, 2, 3]

# n = 5
# lost = [2, 3, 5]
# reserve = [2, 4]


# lost.remove(2)
# print(lost)


# 여벌체육복 가지고온 학생도 도난 가능 -> 그러면 lost, reverse에서 다 제거해야함

for l in lost[:]:
    if l in reserve:
        lost.remove(l)
        reserve.remove(l)

        # print('lost')
        # print(lost)
        # print('reserve')
        # print(reserve)
        # print('-------------------------------')

for rev in reserve:
    if (rev - 1) in lost:
        lost.remove(rev-1)
    elif (rev + 1) in lost:
        lost.remove(rev+1)

ans = n - len(lost)

# print('lost')
# print(lost)
# print('reserve')
# print(reserve)
# print('-------------------------------')
#
print('ans')
print(ans)
print('================================')



