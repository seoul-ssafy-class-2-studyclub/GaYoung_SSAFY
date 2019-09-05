def is_count(k, start, end):
    count = 0
    middle = (start + end) // 2
    while middle != k:  # middle == k이면 stop!!
        count += 1  # 같아지는 순간 count +1 필요
        if k > middle:
            start = middle
        else:
            end = middle
        middle = (start + end) // 2  # 새로운 start와 end를 가지고 middle을 만들어야함 -> middle 초기화!
    count += 1
    return count

for t in range(int(input())):  # 3
    end, a, b = map(int, input().split())  # 400 300 350 (int)
    start = 1
    if is_count(a, start, end) < is_count(b, start, end):
        result = 'A'
    elif is_count(a, start, end) > is_count(b, start, end):
        result = 'B'
    else:
        result = '0'
    print('#{0} {1}'.format(t+1, result))