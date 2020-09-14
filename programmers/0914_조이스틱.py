def count(i):
    if i == 'Z':
        return 1

    else:
        a = ord(i) - ord('A')
        z = ord('Z') - ord(i) + 1
        if a < z + 1:
            return a
        else:
            return z

def solution(name):
    name = list(name)
    answer = 0
    idx = 0

    if name == ['A'] * len(name):
        return 0

    while True:
        left, right = 1, 1
        '''
        [left, right = 0, 0이면 무한으로 도는 이유]
         - if name[idx + i] == 'A': right += 1이다.
           따라서 idx += right 할 때, A가 아닌 다음값으로 가기 위해서는 처음에 right = 1이여야 한다.
        '''

        if name[idx] != 'A':
            answer += count(name[idx])
        name[idx] = 'A'

        '''
        ** 문제점 : ['J', 'A', 'N']에서 ['A', 'A', 'N']에서 ['A', 'A', 'A']로 바뀌고나면 
                    ans=0, idx=0        ans=10, idx=-1     ans=23
                    if name == ['A'] * len(name): 에서 멈춰야하는데, while True: 바로밑에있으면
                    밑에 있는 while문을 한번 더 돈 다음에 break되어 답이 26으로 나온다.
        ** 해결책 : 'A'로 바꾼다음에 if name == ['A'] * len(name):을하면 된다.
        '''
        if name == ['A'] * len(name):
            break


        for i in range(1, len(name)):
            if name[idx + i] == 'A':
                right += 1
            else:
                break

        for i in range(1, len(name)):
            if name[idx - i] == 'A':
                left += 1
            else:
                break

        '''
        [left, right 비교하는 방법]
        1. 스트레이트로 오른쪽으로 가는방법
        2. 오른쪽으로가다가 왼쪽으로 방향전환하는 방법
          -> if left == right:이면 right로 가야한다.
        '''
        if left < right:
            answer += left
            idx -= left  # 그만큼 이동해서 값을 확인한다.

        else:
            answer += right
            idx += right

    return answer



# name = 'JEROEN'
# name = 'JAN'
name = 'BBBAAAB'
# name = 'ABABAAAAABA'

print(solution(name))