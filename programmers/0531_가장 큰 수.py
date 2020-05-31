def solution(numbers):
    str_numbers = [str(i) for i in numbers]

    ls = []
    for i in str_numbers:
        # 3이랑 30이랑 구분할 때, 3이 30보다 크다고 나와야한다
        # -> 그래서 i*4일때 나열하면 3이 30보다 큼

        # 근데 만약에 600이면 [600, 600]으로 나온다.
        # 그러면 60이면 -> 6060..
        # 그러면 모두 같은 자리의숫자가 나올 수 있도록 해야한다
        if len(i) == 4:
            ls.append([i, i * 3])
        if len(i) == 3:
            ls.append([i, i * 4])
        if len(i) == 2:
            ls.append([i, i * 6])
        if len(i) == 1:
            ls.append([i, i * 12])

    # print(ls)

    ls.sort(reverse=True, key=lambda x: x[1])
    # [['9', '9000'], ['5', '5000'], ['34', '3400'], ['3', '3000'], ['30', '3000']]
    # print(ls)

    ans = []
    for l in ls:
        ans.append(l[0])

    return str(int(''.join(ans)))  # 여기서 str을 해주는 이유: '0000'을 0으로 바꾸기 위함

# numbers = [6, 10, 2]
# numbers = [0,0,0,0]
numbers = [12,121]
# numbers = [3, 30, 34, 5, 9]

print(solution(numbers))
