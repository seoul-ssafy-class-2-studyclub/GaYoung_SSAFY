def solution(n, ladder):
    answer = []
    return answer

n = 4
ladder = [[1,0,1],[0,1,0],[0,0,1],[0,0,0],[1,0,0]]

def go(i):
    near = [(1, 1), (1, -1)]

    # print(x, y)
    while True:
        x, y = -1, i - 1

        for a, b in near:
            xi, yi = x+a, y+b
            print(xi, yi)
            if 0 <= xi < n and 0 <= yi < len(ladder) + 1 and ladder[xi][yi] == 1:
                print('yes')
                print('new x, y')
                print('---------------------------')
                x, y = x+1, yi
            else:
                print('no')
                xi += 1

        if x == len(ladder) + 1:
            break


    print(y)
    return y

result = []
for i in range(n):
    result.append(go(i))

print(result)