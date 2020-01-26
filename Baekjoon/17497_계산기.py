'''
N -> 0이 되게 만든다
1. N이 홀수가 되면 무조건 *2를 해서 짝수를 만든다

2. 계산하다가 1이되면 *2 -2를 하면 0이 만들어진다
   계산하다가 2가 되면 -2로 0을 만들면 된다

3. N//2가 홀수라면 N-2를 먼저 하고 //2를 하면 된다.
    ex. N=6이면 N-2를 하면 4가 되고, 계속 나눠가면 된다.

4. N&1 == True는 N%2 == 1과 같은 의미 -> 홀수!!
   N&1 == False ->

   N&2 == True ->
   N&2 == False ->

'''


N = int(input())
ls = []
while N:
    if N & 1:  # 홀수
        ls.append('[/]')
        N *= 2
    elif N & 2:
        ls.append('[+]')
        N -= 2
    else:
        ls.append('[*]')
        N //= 2

if not ls:
    print(-1)
else:
    print(len(ls))
    print(' '.join(ls[::-1]))