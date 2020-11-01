def solution(dirs):
    answer = 0
    return answer

dirs = 'ULURRDLLU'
# dirs = 'LULLLLLLU'

near = {'U':[0, 1], 'R':[1, 0], 'D':[0, -1], 'L':[-1, 0]}
check = []
start = [0, 0]

for i in dirs:
    for key, val in near.items():
        if i == key:
            print(i)
            x, y = start[0] + val[0], start[1] + val[1]
            if -5 <= x <= 5 and -5 <= y <= 5:
                if [start[0], start[0], x, y] not in check:
                    check.append([start[0], start[0], x, y])
                    start = [x, y]
                else:
                    start = [x, y]
            print(start)
            print('-------------------------------------')
print(check)
