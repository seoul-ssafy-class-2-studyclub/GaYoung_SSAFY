# openA = [3, 5, 7]
# closeB = [4, 10, 12]

openA = [4, 7, 9, 16]
closeB = [2, 5, 12, 14, 20]

# openA = [3, 5, 7, 13, 14]
# closeB = [6, 10, 12, 17]

answer = 0
o_idx = 0
c_idx = 0
while True:
    if o_idx == len(openA) and c_idx == len(closeB):
        break

    if openA[o_idx] > closeB[c_idx]:
        # print('go_cidx')
        i = 1

        while True:
            if c_idx + i == len(closeB):
                break

            if openA[o_idx] < closeB[c_idx + i]:
                break

            if openA[o_idx] > closeB[c_idx + i]:
                i += 1
        # if c_idx + 1 < len(closeB):
        c_idx += 1
        answer += (closeB[c_idx] - openA[o_idx])
        o_idx += i
        c_idx += 1


    elif openA[o_idx] < closeB[c_idx]:
        # print('go_oidx')
        i = 1

        while True:
            if o_idx + i == len(openA):
                break

            if openA[o_idx + i] > closeB[c_idx]:
                break

            if openA[o_idx + i] < closeB[c_idx]:
                i += 1

        answer += (closeB[c_idx] - openA[o_idx])
        o_idx += i
        c_idx += 1

print('answer')
print(answer)