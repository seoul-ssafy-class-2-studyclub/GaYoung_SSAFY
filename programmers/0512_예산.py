def solution(d, budget):
    money = 0
    cnt = 0

    # 예산이 작은 것부터 더하면 뒤에거 추가로 볼필요없다.
    d.sort()
    for i in d:
        if money + i <= budget:
            cnt += 1
            money += i
        else:
            break
    return cnt
