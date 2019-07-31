T = int(input())

for t in range(1, T + 1):
    word = input()
    if 3 <= len(word) <= 10:
        if list(word) == list(reversed(word)):
            print('#{0} 1'.format(t))
        else:
            print('#{0} 0'.format(t))