

# files = ['img12.png', 'img10.png', 'img02.png', 'img1.png', 'IMG01.GIF', 'img2.JPG']
# files = ['F-5 Freedom Fighter', 'B-50 Superfortress', 'A-10 Thunderbolt II',' F-14 Tomcat']
files = ['foo9.txt', 'foo010bar020.zip', 'F-15']

def solution(files):

    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    data = []
    for j in range(len(files)):
        head, number = 0, 0
        for i in range(len(files[j])):
            if files[j][i].isnumeric():
                break
            else:
                head = i
        '''
        for i in range(head + 1, len(file)):
            if file[i].isnumeric():
                number = i
            else:
                break
        ** 문제점 : F-15에서 숫자는 15인데, 여기서 인식하는 것은 -부터 숫자라고 인식한다.
        ** 해결책 : 숫자만 뽑게 미리 numbers = []해놓고, 여기 속하는 애들만 number로 칭하기
        '''

        for i in range(head + 1, len(files[j])):
            if files[j][i] in numbers:
                number = i
            else:
                break

        data.append([files[j][:head+1], files[j][head+1:number+1], j])

    data = sorted(data, key=lambda x:(x[0].upper(), int(x[1])))

    answer = []
    for i in data:
        answer.append(files[i[2]])

    return answer