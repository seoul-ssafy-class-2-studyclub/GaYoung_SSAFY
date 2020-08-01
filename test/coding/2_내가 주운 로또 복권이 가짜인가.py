user_input = map(int, input().split())
data = list(user_input)

def solution(data):
    if len(set(data)) != 6:
        return 'false'

    else:
        for i in data:
            if 1 <= i <= 45:
                sort_data = sorted(data)
                if sort_data != data:
                    return 'false'
            else:
                return 'false'

    return 'true'



print(solution(data))