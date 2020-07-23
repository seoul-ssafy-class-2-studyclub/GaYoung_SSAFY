n = 5
arr1 = [9, 20, 28, 18, 11]
arr2 = [30, 1, 21, 17, 28]

print(list(zip(arr1, arr2)))
answer = []
for a, b in zip(arr1, arr2):
    temp = str(bin(a | b))[2:]
    ans = ''
    print(temp)
    # temp.replace('1', '#')
    # temp.replace('0', ' ')

    for i in temp:
        if i == '1':
            i = '#'
        else:
            i = ' '
        ans += i
    answer.append(ans)

print(answer)