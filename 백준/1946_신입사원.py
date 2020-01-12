'''
testcase         A                   B
7     -> 서류1~7등까지 index   면접 1~7등까지 index
3 6             4 *                  7 *         -> (4, 7은 무조건 통과)
7 3             6 a                  3 c'
4 2             1 b                  2
1 4             3 c                  4 *
5 7             5 d                  6 a'
2 5             7 *                  1 b'
6 1             2                    5 d'

첫번째 값이 (4, 7)이므로 7, 4 되기 전 숫자들만 확인!
a -> a'는 B의 * 사이에 없으므로 불가
b -> b'는 B의 * 사이에 없으므로 불가
c -> c'는 B의 * 사이에 있으므로 가능 -> *을 3으로 바꾸기
d -> d'는 B의 * 사이에 없으므로 불가

따라서 정답은 (1, 4), (4, 2), (6, 1)

# 희철오빠 로직
*을 시작점, 끝점으로 나누고 4에 있는 끝점을 3으로 옮기기(시작점은 7 유지)
'''


for t in range(int(input())):
    N = int(input())

    score = [(0, 0)] * N
    visit = [0] * N
    A = [0] * N  # 순위대로 index 나타내기
    B = [0] * N

    for i in range(N):
        a, b = map(int, input().split())
        score[i] = (a - 1, b - 1)
        A[a - 1] = i
        B[b - 1] = i

    # sc1, sc2 = 1등한 값 -> 서류 또는 면접에서 1등한 사람은 무조건 통과!
    sc1 = A[0]  # 4 -> 1등한 사람의 index
    sc2 = B[0]  # 7 -> 1등한 사람의 index
    visit[sc1] = visit[sc2] = 1

    end1 = score[sc2][0]  # 5 -> B(면접)에서 1등한 사람의 A(서류)에서 등수 index
    end2 = score[sc1][1]  # 3 -> A(서류)에서 1등한 사람의 B(면접)에서 등수 index
    # 이 둘의 사이에 있어야함

    start1 = start2 = 1  # 서류, 면접의 index!!
    # 1등의 index는 0이다
    while True:
        # 앞으로 계속 start1, end2값만 바꿀 것
        # 7일때 7이면 stop
        if start1 == end1:
            break

        man = A[start1]
        # B에서 7이랑 4 사이에 있을 때만 end2를 바꾸어줌
        if score[man][1] < end2:
            visit[man] = 1
            end2 = score[man][1]

        # A에서 6일 때 B에서 *보다 밑에있음
        if end2 <= start2:
            break

        start1 += 1

    print(sum(visit))

