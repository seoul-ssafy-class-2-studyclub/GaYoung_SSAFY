def solution(phone_book):
    phone_book.sort()
    for i in range(len(phone_book) - 1):
        cnt = len(phone_book[i])
        if phone_book[i] in phone_book[i + 1][:cnt]:
            return False

    return True

phone_book = ['119', '97674223', '1195524421']
# phone_book = ['123', '456', '789']
# phone_book = ['12', '123', '1235', '567', '88']

print(solution(phone_book))