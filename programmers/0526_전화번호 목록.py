phone_book = ['119', '97674223', '1195524421']
# phone_book = ['123', '456', '789']
# phone_book = ['12', '123', '1235', '567', '88']


# 1. sort사용
def solution(phone_book):
    phone_book.sort()
    for p in range(len(phone_book)-1):
        # print(phone)
        cnt = len(phone_book[p]) # 119
        if phone_book[p] in phone_book[p + 1][:cnt]:
            return False
    return True


# 2. startswitch 사용
def use_startswitch(phone_book):
    phone_book.sort()
    pair = list(zip(phone_book, phone_book[1:]))  # p번째와 p+1번째 두개를 zip
    # print(pair)
    for p1, p2 in pair:
        if p2.startswith(p1):  # p2가 p1으로 시작하는가? -> True면 return False
            return False
    return True


# 3. hash사용
def use_hash(phone_book):
    dic = {}
    for phone in phone_book:
        dic[phone] = 1

    for phone in phone_book:
        temp = ''
        for p in phone:
            temp += p
            '''
            9
            97
            976
            9767
            97674
            976742
            9767422
            97674223
            이런식으로 나온다. 이때, 119가 포함되어있으면 return false
            '''
            if temp in dic and temp != phone:
                return False
        return True

print(use_hash(phone_book))

