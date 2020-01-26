'''
[ dfs 재귀로 풀기 ]
1. board가 100*100이면 재귀 사용 금지!(depth=3000이상이면 재귀 X)

[ dfs 풀 때, 결과값 설정하는 방법 ]
1. 값 갱신
    1-1. mymin = 99999999 or mymax = 0으로 둔다
    1-2. def func()에서 global mymin or global mymax 설정
    1-3. mymin과 sum(cnt) 등을 비교하면서 mymin 갱신
    1-4. return mymin -> print(func()) or print(mymin)

2. 재귀함수
    2-1. 재귀함수를 빠져나올 조건 설정 -> return
    2-2. 재귀함수를 사용하는 곳에 변수로 재귀 실행 필요 (return 사용!)
    2-3. 값을 갱신하지는 않지만, 이전 값을 기억해 그 값을 가지고옴!
         * 이전값을 기억하지 못하고 계속 돈다면, 그것은 None으로 리턴

3. list 이용
    3-1. dfs를 진행하면서 내가 필요한 값들을 return하지않고 list에 넣기
    3-2. 이때, 필요한 것은, 내가 필요한 값을 초기화하는것!
         (그래야 새로 시작)
'''

'''
'''