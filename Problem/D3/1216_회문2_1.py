def is_p(word):
    for i in range((len(word) // 2)):
        if word[i] != word[-1-i]:
            return False
    return len(word)

def longest_p(row):
    l_p = 0
    for t_v in range(2, len(row)):
        for x in range(len(row) - t_v + 1):
            word = is_p(row[x:x+t_v])
            if word:
                l_p = word
                break
    return l_p

for t in range(10):
    N = int(input())
    result = 0
    board = []

    for _ in range(100):
        row = input()
        board.append(row)
        l = longest_p(row)
        if l > result:
            result = l
            
    for j in range(100):
        col = ''
        for i in range(100):
            col += board[i][j]
        l = longest_p(col)
        if l > result:
            result = l
    print('#{} {}'.format(N, result))
    