def solution(s, n):
    answer = ''
    for i in s:
        if i ==' ':
            answer += ' '
        else:
            if 65 <= ord(i) <= 90:
                if ord(i) + n > 90:
                    answer += chr(ord(i) - 26 + n)
                else:
                    answer += chr(ord(i) + n)
            else:
                if ord(i) + n > 122:
                    answer += chr(ord(i) - 26 + n)
                else:
                    answer += chr(ord(i) + n)

    return ''.join(answer)


s = 'a B z'
n = 4

s = list(s)
print(s)
print(ord('a'))
print(ord('z'))
print(ord('A'))
print(ord('Z'))
