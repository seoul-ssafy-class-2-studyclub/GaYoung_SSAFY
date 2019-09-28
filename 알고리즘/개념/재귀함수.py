def countdown(i):
    print(i)
    if i <= 1:
        return i
    else:
        countdown(i-1)

print(countdown(5))
'''
5
4
3
2
1
None
'''

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