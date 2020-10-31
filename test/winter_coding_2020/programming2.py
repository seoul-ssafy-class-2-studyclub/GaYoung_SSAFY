def solution(encrypted_text, key, rotation):
    words = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10, 'k': 11, 'l': 12, 'm': 13,
             'n': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20, 'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25,
             'z': 26}
    while True:
        if rotation >= 0:
            if rotation < len(encrypted_text):
                break

            rotation -= len(encrypted_text)
        else:
            if rotation > 0:
                break
            rotation += len(encrypted_text)

    encrypted_text = encrypted_text[rotation:] + encrypted_text[:rotation]

    encrypted_text = list(encrypted_text)
    for i in range(len(key)):
        encrypted_text[i] = ord(encrypted_text[i]) - words[key[i]]

        if encrypted_text[i] < 97:
            encrypted_text[i] = 122 - 97 + encrypted_text[i] + 1

        encrypted_text[i] = chr(encrypted_text[i])
    encrypted_text = ''.join(encrypted_text)
    # print(encrypted_text)
    return encrypted_text


encrypted_text = 'qyyigoptvfb'
key = 'abcdefghijk'
rotation = 13
# pwvebiilmvq
words = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10, 'k': 11, 'l': 12, 'm': 13,
             'n': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20, 'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25,
             'z': 26}
while True:
    if rotation > 0:
        if rotation < len(encrypted_text):
            break

        rotation -= len(encrypted_text)
    else:
        if rotation > 0:
            break
        rotation += len(encrypted_text)

encrypted_text = encrypted_text[rotation:] + encrypted_text[:rotation]

encrypted_text = list(encrypted_text)
for i in range(len(key)):
    encrypted_text[i] = ord(encrypted_text[i]) - words[key[i]]

    if encrypted_text[i] < 97:
        encrypted_text[i] = 122 - 97 + encrypted_text[i] + 1

    encrypted_text[i] = chr(encrypted_text[i])
encrypted_text = ''.join(encrypted_text)
print(encrypted_text)