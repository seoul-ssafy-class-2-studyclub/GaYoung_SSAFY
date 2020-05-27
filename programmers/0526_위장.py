def solution(clothes):
    dic = {}  # dict = {headgear:['yellow_hat', 'green_turban'], eyewear:['blue_sunglasses']}
    for cloth in clothes:
        key = cloth[1]
        value = cloth[0]
        if key in dic:
            dic[key].append(value)
        else:
            dic[key] = [value]

    # dic = {headgear:['yellow_hat', 'green_turban'], eyewear:['blue_sunglasses']}
    # total = (headgear+1) * (eyewear+1) -1
    ans = 1
    for key in dic.keys():
        ans *= (len(dic[key]) + 1)

    # print(ans - 1)

    return ans - 1

# clothes = [['yellow_hat', 'headgear'], ['blue_sunglasses', 'eyewear'], ['green_turban', 'headgear']]
clothes = [['crow_mask', 'face'], ['blue_sunglasses', 'face'], ['smoky_makeup', 'face']]

