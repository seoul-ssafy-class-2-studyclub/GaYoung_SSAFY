# gems = ["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]  # [3, 7]
# gems = ["AA", "AB", "AC", "AA", "AC"]  # [1, 3]
# gems = ["XYZ", "XYZ", "XYZ"]  # [1, 1]
# gems = ["ZZZ", "YYY", "NNNN", "YYY", "BBB"]  # [1, 5]
gems = ['d', 'r', 'r', 'd', 'd', 'e', 's', 'd', 'd', 'e', 's', 'r']

'''
[d r r d d e s] d d e s r
d [r r d d e s] d d e s r
d r [r d d e s] d d e s r -> [2, 6] (5) -> answer = [3, 7]
d r r [d d e s d d e s r]
d r r d [d e s d d e s r]
d r r d d [e s d d e s r]
d r r d d e [s d d e s r]
d r r d d e s [d d e s r]
d r r d d e s d [d e s r] -> [8, 11] (4) -> answer = [9, 12]

최종 답 : [9, 12]
'''


def solution(gems):
    result = [0, len(gems) - 1]
    start, end = 0, 0
    len_set_gems = len(set(gems))  # 4

    check = {gems[0]: 1}
    while start < len(gems) and end < len(gems):
        print('check, start, end')
        print(check, start, end)
        if len(check) == len_set_gems:
            print('same')
            if result[1] - result[0] > end - start:  # 차이가 적은 start, end값으로 갱신
                result[0], result[1] = start, end

            if check[gems[start]] != 1:
                check[gems[start]] -= 1
                start += 1

            elif check[gems[start]] == 1:
                del check[gems[start]]
                start += 1


        elif len(check) < len_set_gems:
            print('not-same')
            end += 1

            if end == len(gems):  # end == len(gems)면 계산할 필요가 없다.
                break

            if gems[end] not in check:
                check[gems[end]] = 1

            else:
                check[gems[end]] += 1

    result[0] += 1
    result[1] += 1

    return result

print(solution(gems))