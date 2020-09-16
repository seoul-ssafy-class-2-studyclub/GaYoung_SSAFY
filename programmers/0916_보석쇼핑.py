def solution(gems):
    answer = []
    return answer

gems = ["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]
# gems = ["AA", "AB", "AC", "AA", "AC"]
# gems = ["XYZ", "XYZ", "XYZ"]
# gems = ["ZZZ", "YYY", "NNNN", "YYY", "BBB"]

'''
gems가 종류별로 있다면 result[0] += 1하고 확인하기
       종류별로 없다면 result[]장
'''
result = [0, len(gems) - 1]
gems_set = len(set(gems))
check = {gems[0]:1}
start, end = 0, 0
while start < len(gems) and end < len(gems):

    if len(check) < gems_set:
        end += 1

        if end == len(gems):  # 더이상 갈 수 없음
            break

        if check.get(gems[end]) is None:
            check[gems[end]] = 1
        else:
            check[gems[end]] += 1


    if len(check) == gems_set:
        if result[1] - result[0] > end - start:
            result[1] = end
            result[0] = start

        # {'D':2, 'R':1, 'T':1, 'O':1}이면 {'D':1, 'R':1, 'T':1, 'O':1}이 된다면 최소값으로 답이다.
        if check[gems[start]] != 1:
            check[gems[start]] -= 1
            start += 1
        elif check[gems[start]] == 1:
            del check[gems[start]]  # 여기에서 값을 지워줘야 다음으로 넘어갈 수 있다.
            start += 1

    # print(check)
result[0] += 1
result[1] += 1
print(result)