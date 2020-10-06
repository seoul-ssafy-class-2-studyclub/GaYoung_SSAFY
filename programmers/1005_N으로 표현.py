N = 5
number = 12

# N = 5
# number = 11
'''
1번 사용 : 5
2번 사용 : 55, 5+5=10, 5-5=0, 5*5=25, 5/5=1
3번 사용 : 555, 5+5+5=15, 5+5-5=5, 5+5*5=30, 5+5/5=6, 5-5+5=5, 5-5-5=-5, 5-5*5=-20, 5-5/5=4,
               5*5+5=30, 5*5-5=20, 5*5*5=125, 5*5/5=5, 5/5+5=6, 5/5-5=-4, 5/5*5=5, 5/5/5=0,
          555 + 1번사용->2번사용, 2번사용->1번 사용(중복은 제거)
4번 사용 : 555 + 1번사용->3번사용, 2번사용->2번 사용, 3번사용->1번 사용(중복은 제거)
'''

def solution(N, number):
    check = []
    for i in range(1, 9):
        num_ls = {int(str(N) * i)}

        for j in range(0, i-1):
            for x in check[j]:
                for y in check[-j-1]:
                    num_ls.add(x + y)
                    num_ls.add(x - y)
                    num_ls.add(y - x)
                    num_ls.add(x * y)

                    if y != 0:
                        num_ls.add(x // y)

                    if x != 0:
                        num_ls.add(y // x)

        if number in num_ls:
            return i

        check.append(num_ls)

    return -1

print(solution(N, number))