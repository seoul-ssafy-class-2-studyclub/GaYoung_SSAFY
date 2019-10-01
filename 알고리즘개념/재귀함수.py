'''
[재귀 사용 시, return func()과 func()의 차이]
1. return func(): 특정 값 저장하고 return
2. func(): 그냥 나아감
'''

data = [1, 2, 3]
visit = [False] * 3
result = []
def func(arr):
    if len(arr) == 3:
        result.append(arr)
        return result
    for i in range(3):
        if visit[i] == False:
            visit[i] = True
            func(arr)
'''
             1 ---------------> 2 ---------------> 3
return O [1, 2, 3] <------ [1, 2, 3] <-------  return func() => [1, 2, 3]
    i가 3까지 돌고나서 값을 return(저장)해준 다음에 다시 위로 감!

return X None <------------- None <------------- func() => [1, 2, 3]
   i가 3까지 돌고나서 값을 저장하지 못했기 때문에 i는 4로 향함 -> None
'''







'''
재귀함수 사용시 주의점!
1. result += board[xi][yi]
   dfs(xi, yi, result, cnt + 1)
   
2. dfs(xi, yi, result + board[xi][yi], cnt + 1)
'''
board = [list(input().split()) for _ in range(4)]
near = [(-1, 0), (0, 1), (1, 0), (0, -1)]
def dfs(x, y, result, cnt):

    if cnt == 7:
        if result not in visit:
            visit.append(result)
            return

    else:
        for a, b in near:
            xi = x + a
            yi = y + b
            if 0 <= xi < 4 and 0 <= yi < 4:
                dfs(xi, yi, result + board[xi][yi], cnt + 1)
'''
이때, 올바른 방법은 2번
why? 1. 1121에서 1이 추가되면 11211-> 112111, 112112..로 나아감
     2. 1121로 고정하고, 11211, 11212로 나아감..
   2번으로 해야 값이 저장되면서 바뀜!
'''