def solution(files):
    temp = []
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    for file in range(len(files)):
        head, number = 0, 0

        for i in range(len(files[file])):  # img12.png
            if files[file][i].isnumeric():
                break
            else:
                head = i

            '''
            if files[file][i].isalpha():
                head = i
            elif files[file][i].isnumeric():  # isnumeric -> F-15를 ('F', '-1')로 쪼갬
                break
                
            ** 문제점 : F-15를 ('F-', '1')로 쪼개야하는데 ('F', '-1')로 쪼갠다 -> '-'를 isalpha()하면 false가 나온다.
            ** 해결책 : 숫자가 아닌것들을 다 확인해서 head로 보낸다
            '''
        for i in range(head + 1, len(files[file])):
            if files[file][i] in numbers:
                number = i
            else:
                break

        temp.append((files[file][:head + 1], files[file][head + 1:number + 1], file))

    temp_sort = sorted(temp, key=lambda x: (x[0].upper(), int(x[1]), x[2]))

    answer = []
    for i in temp_sort:
        answer.append(files[i[2]])

    return answer


# files = ['img12.png', 'img10.png', 'img02.png', 'img1.png', 'IMG01.GIF', 'img2.JPG']
# files = ['F-5 Freedom Fighter', 'B-50 Superfortress', 'A-10 Thunderbolt II', 'F-14 Tomcat']
files = ['foo9.txt', 'foo010bar020.zip', 'F-15']

print(solution(files))
