'''
예시1. 가격 알아보기
'''
book = {}
book['apple'] = 0.67
book['milk'] = 1.49
book['avocado'] = 1.12

print(book)  # 해쉬: {'apple': 0.67, 'milk': 1.49, 'avocado': 1.12}
print(book['avocado'])  # avocado 가격 알기



'''
예시2. 투표관리하며 중복된 항목 방지
'''
voted = {}

def check_voter(name):
    if voted.get(name):
        return '돌려 보내세요!'
    else:
        voted[name] = True
        return '투표하게 하세요~'

print(check_voter('tom'))
print(check_voter('jenny'))
print(check_voter('jenny'))
'''
함수 안에서 return 하면 결과값만 나옴! print 하면 결과값+None이 나옴
'''



'''
예시3. 홈페이지_캐시사용
'''
cache = {}

def get_page(url):
    if cache.get(url):
        return cache[url]  # 캐싱된 자료를 전송
    else:
        data = get_data_from_server(url)
        cache[url] = data  # cache에 처음으로 자료를 저장
        return data


'''
[ 좋은 해쉬함수 ]
1. 배열에 값을 고루 분포시키는 함수(값들이 뭉쳐져 있으면 충돌이 자주 발생)
'''

near = [(-1, 0), (0, 1), (1, 0), (0, -1)]


def dfs(x, y, cnt=1, start)
    # if cache[]
    #     return cnt
    flag = 0
    if cache.get(board[x][y]) != None:
        return cache[board[x][y]]
    res = 1
    for a, b in near:
        xi = x + a
        yi = y + b
        if 0 <= xi < N and 0 <= yi < N:
            if board[xi][yi] == board[x][y] + 1:
                res = 1 + dfs(xi, yi, cnt + 1, start)

    cache[board[x][y]] = res
    if res > max:
        max = res

    return res


for t in range(int(input())):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]

    cache = {}
    for x in range(N):
        for y in range(N):
            if board[x][y]:
                cache[board[x][y]] = dfs(x, y, 1, board[x][y])
    print(cache)