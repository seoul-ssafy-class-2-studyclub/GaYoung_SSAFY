# m = "kkaxbycyz"
# k = "abc"

# m = "acbbcdc"
# k = "abc"

m = "aabcb"
k = "ab"

answer = ''
m_idx = -1
k_idx = 0
while True:
    m_idx += 1

    if m[m_idx] == k[k_idx]:
        k_idx += 1
        if k_idx == len(k):
            answer += m[m_idx+1:]
            break

    elif m[m_idx] != k[k_idx]:
        answer += m[m_idx]

print(answer)