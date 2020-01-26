'''
[ 비트 연산자 ]
& (Binary AND) : 둘다 참일때만 만족  ex) (a & b) = 12 → 0000 1100
| (Binary OR) : 둘 중 하나만 참이여도 만족  ex) (a | b) = 61 → 0011 1101
^ (Binary XOR) : 둘 중 하나만 참일 때 만족  ex) (a ^ b) = 49 → 0011 0001
~ (Binary NOT) : bit 단위로 not연산을 합니다.(1의 보수)  ex) (~a) = -61 → 1100 0011
<< (Binary left Shift) : 변수의 값을 왼쪽으로 지정된 비트 수 만큼 이동  ex) a << 2 = 240 → 1111 0000
>> (Binary right Shift) : 변수의 값을 오른쪽으로 지정된 비트 수 만큼 이동  ex) a >> 2 = 15 → 0000 1111
'''


'''
[ 문제 ]
1.이 성에 있는 방의 개수
2.가장 넓은 방의 넓이
3.하나의 벽을 제거하여 얻을 수 있는 가장 넓은 방의 크기

[풀이법]
1, 2. cnt_ls = [방 넓이, 방 넓이, 방 넓이,, ] -> 1.len(cnt_ls), 2.mymax 갱신
'''


# 벽에대한 정보: 서쪽->1, 북쪽->2를, 동쪽->4, 남쪽->8 을 더한 값 -> 비트
near = [(0, -1), (-1, 0), (0, 1), (1, 0)]  # 서, 북, 동, 남 순서대로 near

N, M = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(M)]
visit = [[False] * N for _ in range(M)]
room_board = [[0] * N for _ in range(M)]

'''
[ 이동하기 ]
1. visit이 False일 때, 첫 시작을 한다.
2. 이동하는 방법은, 동서남북 중에 벽이 없는 곳으로 이동.
   how? 11과 1<<(1~4)일 때를 비교 -> 1011
                                       1 -> True
                                      1  -> True
                                     1   -> False -> 이때 옆칸으로 이동! (near과 같은 역할!)
                                    1    -> True
'''

room_cnt = 0
mymax = 0
room_space = 0
queue = []
ls = {}  # 벽을 뚫어 방을 연결할 때, 방마다 방의 크기가 필요 => ex. ls = {1:9, 2:3,,,}
for i in range(M):
    for j in range(N):
        if visit[i][j] == False:
            queue.append((i, j))
            visit[i][j] = True
            room_space = 1
            room_cnt += 1
            room_board[i][j] = room_cnt
            while queue:
                x, y = queue.pop(0)
                room = board[x][y]
                for n in range(4):
                    if room & (1 << n) == False:
                        xi, yi = (x + near[n][0], y + near[n][1])
                        if 0 <= xi < M and 0 <= yi < N and visit[xi][yi] == False:
                            visit[xi][yi] = True
                            queue.append((xi, yi))
                            room_board[xi][yi] = room_cnt
                            room_space += 1

        ls[room_cnt] = room_space  # {1: 9, 2: 3, 3: 8, 4: 1, 5: 7}
        if mymax < room_space:
            mymax = room_space


print(room_cnt)
print(mymax)


'''
[ 방 잇기 ]
1. 하나의 벽을 깨서 방을 잇기 위해서는 방 번호가 같은지 확인한다 
    1-1. 만약 다르면 그 방끼리의 갯수 더하기 (ls부터 가지고오면 됨)
'''
broken = 0
for i in range(M):
    for j in range(N):
        for n in range(2, 4):
            ii = i + near[n][0]
            jj = j + near[n][1]
            if 0 <= ii < M and 0 <= jj < N and room_board[i][j] != room_board[ii][jj]:
                temp = ls[room_board[i][j]] + ls[room_board[ii][jj]]
                if broken < temp:
                    broken = temp

print(broken)
