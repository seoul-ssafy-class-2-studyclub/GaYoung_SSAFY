# def solution(numbers):
#     answer = ''
#     return answer

numbers = [6, 10, 2]
# numbers = [3, 30, 34, 5, 9]

str_numbers = [str(i) for i in numbers]

ans = ''
while len(numbers) != 0:
    check = 0
    for number in str_numbers:
        first = int(number[0])
        if first > check:
            check = first

    print(check)


