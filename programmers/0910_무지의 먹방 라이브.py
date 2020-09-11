# food_times = [4, 3, 5, 6, 2]
# k = 7

food_times = [3, 1, 2]
k = 5

# food_times = [1,1,1,1]
# k = 4

'''
[3, 1, 2] -> [2, 0, 1]로 한번에 가려면 len(food_times)만큼 건너뛰면 된다.
'''

def solution(food_times, k):

    total = sum(food_times)

    # 전체 먹는 시간보다 k가 크면 계산 불가능 이므로 -1
    if total <= k:
        return -1

    food_times = [(food, idx) for idx, food in enumerate(food_times, 1)]
    food_times = sorted(food_times, key=lambda x:x[0])
    food = 1
    down = food_times[0][0] * len(food_times)

    while down < k:
        k -= down
        down = (food_times[food][0] - food_times[food - 1][0]) * (len(food_times) - food)
        food += 1  # 사라진 음식 수

    # food번만큼 떨어뜨렸으니까 떨어뜨릴만큼 다 떨어뜨린 결과물이다.
    # 이걸 인덱스 순으로 나열한 다음에 k번째 음식의 인덱스 찾기
    food_times = sorted(food_times[food-1:], key=lambda x: x[1])

    return food_times[k % len(food_times)][1]