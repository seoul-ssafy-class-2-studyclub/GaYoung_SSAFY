def is_Palindrome(word):
    for i in range(len(word) // 2):
        if word[i] != word[-i-1]:
            return False
    return True

    
T = int(input())

for t in range(1, T + 1):
    word = input()
    if 3 <= len(word) <= 10:
        if list(word) == list(reversed(word)):
            print('#{0} 1'.format(t))
        else:
            print('#{0} 0'.format(t))