words = ["frodo", "front", "frost", "frozen", "frame", "kakao"]
queries = ["fro??", "???ao", "fr???", "fro???", "pro?"]
# queries = ["???ao"]
# 검색 키워드는 와일드카드 문자인 '?'가 하나 이상 포함돼 있으며,
# '?'는 각 검색 키워드의 접두사 아니면 접미사 중 하나로만 주어집니다.

def solution(words, queries):
    answer = []
    for query in queries:
        cnt = 0
        length = len(query)

        if query[0] == '?':  # 접두사
            check = query.split('?')[-1]
            for word in words:
                if len(check) == 0 and len(word) == length:
                    cnt += 1
                elif word[length - len(check):] == check and len(word) == length:
                    cnt += 1

        else:  # 접미사
            check = query.split('?')[0]
            for word in words:
                if len(check) == 0 and len(word) == length:
                    cnt += 1
                elif len(word) == length and word[:len(check)] == check:
                    cnt += 1

        answer.append(cnt)
    # print(answer)
    return answer

print(solution(words, queries))