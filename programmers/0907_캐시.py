# cacheSize = 3
# cities = ['Jeju', 'Pangyo', 'Seoul', 'NewYork', 'LA', 'Jeju', 'Pangyo', 'Seoul', 'NewYork', 'LA']

# cacheSize = 3
# cities = ['Jeju', 'Pangyo', 'Seoul', 'Jeju', 'Pangyo', 'Seoul', 'Jeju', 'Pangyo', 'Seoul']

# cacheSize = 2
# cities = ['Jeju', 'Pangyo', 'Seoul', 'NewYork', 'LA', 'SanFrancisco', 'Seoul', 'Rome', 'Paris', 'Jeju', 'NewYork', 'Rome']

# cacheSize = 5
# cities = ['Jeju', 'Pangyo', 'Seoul', 'NewYork', 'LA', 'SanFrancisco', 'Seoul', 'Rome', 'Paris', 'Jeju', 'NewYork', 'Rome']

# cacheSize = 2
# cities = ['Jeju', 'Pangyo', 'NewYork', 'newyork']

# cacheSize = 0
# cities = ['Jeju', 'Pangyo', 'Seoul', 'NewYork', 'LA']

cacheSize = 5
cities = ["SEOUL", "SEOUL", "SEOUL" ]

'''
LRU(Least Recently Used) 알고리즘
 : 캐시의 사이즈는 한정 되어있기 때문에 캐시 사이즈가 꽉 찬 상태에서 새로운 캐시를 넣으려면
   기존 캐시에 있던 데이터를 교체해야하는 데, 가장 오래전에 사용한 것을 제거하는 알고리즘
'''
def solution(cacheSize, cities):
    cities = [city.lower() for city in cities]
    check = []

    answer = 0
    if cacheSize == 0:
        answer += len(cities) * 5

    else:
        for city in cities:
            if city in check:
                answer += 1
                check.pop(check.index(city))
                check.append(city)
            else:
                answer += 5
                if len(check) >= cacheSize:
                    check.pop(0)  # 가장 오래된 것 빼내기
                    check.append(city)
                else:
                    check.append(city)

    # print(answer)
    return answer

print(solution(cacheSize, cities))