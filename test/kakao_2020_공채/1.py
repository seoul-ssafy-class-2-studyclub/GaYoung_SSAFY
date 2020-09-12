def solution(new_id):
    answer = ''
    return answer

# new_id = '...!@BaT#*..y.abcdefghijklm.'
# new_id = 'z-+.^.'
# new_id = '=.='
new_id = '123_.def'
# new_id = 'abcdefghijklmn.p'
# new_id = '...'
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
id = ''
for i in new_id:
    if i.isalpha() or i in numbers or i in ['-', '_', '.']:  # 2단계
        if id and id[-1] == '.' and i == '.':  # 3단계
            continue

        id += i.lower()  # 1단계

# 4단계
if id[0] == '.' and id[-1] == '.':
    id = id[1:-1]
elif id[0] == '.':
    id = id[1:]
elif id[-1] == '.':
    id = id[:-1]

if id == '':
    id += 'a'  # 5단계

if len(id) >= 16:  # 6단계
    id = id[:15]
    if id[-1] == '.':
        id = id[:14]


add_num = 3 - len(id)  # 7단계
if len(id) <= 2:
    id += id[-1] * add_num

print(id)