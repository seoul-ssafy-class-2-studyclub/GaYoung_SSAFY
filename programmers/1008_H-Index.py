citations = [3, 0, 6, 1, 5, 2]
# citations = [0]

# 이곳에 없는 숫자가 H-Index일 수 있다.
def solution(citations):
    mymax = max(citations)

    for i in range(mymax, -1, -1):
        if i == 0:
            return 0

        cnt = 0
        for citation in citations:
            if citation >= i:
                cnt += 1

            if cnt == i:
                return i

print(solution(citations))