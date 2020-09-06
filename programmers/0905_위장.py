def solution(clothes):
    answer = 1
    total = {}
    for clothe in clothes:
        name, type = clothe
        if type not in total:
            total[type] = [name]
        else:
            total[type].append(name)

    for i in total.values():
        answer *= len(i) + 1

    return answer - 1

# clothes = [['yellow_hat', 'headgear'], ['blue_sunglasses', 'eyewear'], ['green_turban', 'headgear']]
# clothes = [['yellow_hat', 'headgear'], ['blue_sunglasses', 'headgear'], ['green_turban', 'headgear']]
clothes = [['crow_mask', 'face'], ['blue_sunglasses', 'face'], ['smoky_makeup', 'face']]


