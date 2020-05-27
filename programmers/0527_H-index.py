def solution(citations):

    mmax = max(citations)
    for ci in range(mmax, -1, -1):

        # ci=1일때 return 0 을 따로 조건을 주기!
        # -> 이 조건이 없으니까 테케16번 실패함..
        if ci == 0:
            return 0

        mymax = 0
        for citation in citations:
            if ci <= citation:
                mymax += 1

            if mymax == ci:
                return ci


citations = [3, 0, 6, 1, 5]
print(solution(citations))
