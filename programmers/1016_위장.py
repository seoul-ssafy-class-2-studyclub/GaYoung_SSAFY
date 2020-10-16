def solution(clothes):
    check = {}
    for a, b in clothes:
        if b not in check:
            check[b] = 1
        else:
            check[b] += 1

    answer = 1
    for key, val in check.items():
        answer *= (val + 1)

    return answer - 1

clothes = [['yellow_hat', 'headgear'], ['blue_sunglasses', 'eyewear'], ['green_turban', 'headgear']]
