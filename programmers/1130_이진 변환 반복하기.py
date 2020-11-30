def solution(s):
    cnt = 0
    zero_count = 0

    while s != '1':
        cnt += 1
        one_count = 0

        for i in s:
            if i == '1':
                one_count += 1
            else:
                zero_count += 1

        s = str(bin(one_count)[2:])

    # print([cnt, zero_count])
    return [cnt, zero_count]

# s = "110010101001"  # [3,8]
# s = "01110"  # [3,3]
s = "1111111"  # [4,1]


