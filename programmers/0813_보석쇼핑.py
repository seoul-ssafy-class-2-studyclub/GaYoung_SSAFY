'''
[투포인터 기법]
두개의 포인터를 만들어 각각이 가리키는 원소에 의미를 부여해 푸는 알고리즘
1) 포인터 2개가 같은방향으로 진행
2) 포인터 2개가 양끝에서 반대로 진행
3) 포인터 하나는 한쪽방향으로만 진행, 다른포인터는 양쪽으로 이동
'''

'''
보석을 다 안가지고 있으면 end를 올려주고
보석을 다 가지고 있으면 start를 올려준다고 생각하면 돼

'''
gems = ["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]
# gems = ["AA", "AB", "AC", "AA", "AC"]
# gems = ["XYZ", "XYZ", "XYZ"]
# gems = ["ZZZ", "YYY", "NNNN", "YYY", "BBB"]

gems_set = len(set(gems))  # {D, R, E, S}
start, end = 0, 0
check = {gems[0]: 1}
answer = [0, len(gems)-1]
# [0, len(gems)]하면 맨 밑에서 answer[1], answer[0] += 1씩 해주기 때문에 보석 쇼핑이 맨 마지막에서 끝나면 len(gems)=6이더라도 답이 [,7]로 나온다
while start < len(gems) - 1 and end < len(gems) - 1:

    if len(check) == gems_set:
        if answer[1] - answer[0] > end - start:
            answer[1] = end
            answer[0] = start
        if check[gems[start]] != 1:
            check[gems[start]] -= 1
            start += 1
        elif check[gems[start]] == 1:
            del check[gems[start]]  # 여기에서 값을 지워줘야 다음으로 넘어갈 수 있다.
            '''
            ex. d,r,r,d,d,e,s,d,d,e,s,r이 테케라면 
              [d,r,r,d,d,e,s],d,d,e,s,r
              d,[r,r,d,d,e,s],d,d,e,s,r
              d,r,[r,d,d,e,s],d,d,e,s,r -> [2, 6] (5)
              d,r,r,[d,d,e,s,d,d,e,s,r]
              d,r,r,d,[d,e,s,d,d,e,s,r]
              d,r,r,d,d,[e,s,d,d,e,s,r]
              d,r,r,d,d,e,[s,d,d,e,s,r]
              d,r,r,d,d,e,s,[d,d,e,s,r]
              d,r,r,d,d,e,s,d,[d,e,s,r] -> [8, 11] (4)
              이렇게 나오게하려면 앞에 값을 삭제하고 뒤에 나오는 값들을 다시 넣어줘야한다.
            '''
            start += 1

    # while을 돌면서 len(check) < gems_set을 처리하는게 아니라
    # 마지막에 보석을 다 모으게 되면 while을 돌면서 start를 올려줘야한다.
    # 마지막에 보석을 다 모으면 end + 1상태로 끝나서 elif len(check)==gems_set에 안걸린다.
    # 따라서 if end == len(gems): break 를 while문 밑에다 하는게 아니라 end += 1하고난 후에 비교해야함
    if len(check) < gems_set:
        end += 1

        if end == len(gems):
            break

        if check.get(gems[end]) is None:  # 중복이 많아지면 n번 돌기때문에 효율성 꽝
            check[gems[end]] = 1
        else:
            check[gems[end]] += 1

answer[0] += 1
answer[1] += 1

print(answer)


def solution(gems):
    gems_set = len(set(gems))  # {D, R, E, S}
    start, end = 0, 0
    check = {gems[0]: 1}
    answer = [0, len(gems) - 1]
    # [0, len(gems)]하면 맨 밑에서 answer[1], answer[0] += 1씩 해주기 때문에 보석 쇼핑이 맨 마지막에서 끝나면 len(gems)=6이더라도 답이 [,7]로 나온다
    while start < len(gems) and end < len(gems):

        if len(check) == gems_set:
            if answer[1] - answer[0] > end - start:
                answer[1] = end
                answer[0] = start
            if check[gems[start]] != 1:
                check[gems[start]] -= 1
                start += 1
            elif check[gems[start]] == 1:
                del check[gems[start]]  # 여기에서 값을 지워줘야 다음으로 넘어갈 수 있다.
                start += 1

        # while을 돌면서 len(check) < gems_set을 처리하는게 아니라
        # 마지막에 보석을 다 모으게 되면 while을 돌면서 start를 올려줘야한다.
        # 마지막에 보석을 다 모으면 end + 1상태로 끝나서 elif len(check)==gems_set에 안걸린다.
        # 따라서 if end == len(gems): break 를 while문 밑에다 하는게 아니라 end += 1하고난 후에 비교해야함
        if len(check) < gems_set:
            end += 1
            if end == len(gems):
                break

            if check.get(gems[end]) is None:  # 중복이 많아지면 n번 돌기때문에 효율성 꽝
                check[gems[end]] = 1
            else:
                check[gems[end]] += 1

    answer[0] += 1
    answer[1] += 1

    return answer

