def solution(numbers, target):
    ls = [0]
    for num in numbers:
        ans = []
        for l in ls:
            ans.append(l + num)
            ans.append(l - num)
        ls = ans
    print(ls)

    cnt = 0
    for i in ls:
        if i == target:
            cnt += 1

    # print(cnt)

    return cnt



numbers = [1, 1, 1, 1, 1]
target = 3

