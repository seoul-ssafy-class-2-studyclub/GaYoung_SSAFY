def solution(A, B):
    A = sorted(A, reverse=True)
    B = sorted(B, reverse=True)

    cnt = 0
    for a in A:
        for b in B:
            if a < b:  # b가 더 크면 cnt += 1
                cnt += 1
                B.remove(b)
                break  # for b in B 해야한다
    # print(cnt)

    return cnt

# A = [5,1,3,7]
# B = [2,2,6,8]

A = [2,2,2,2]
B = [1,1,1,1]



