# m = 'ABCDEFG'
# musicinfos = ['12:00,12:14,HELLO,CDEFGAB', '13:00,13:05,WORLD,ABCDEF']

m = 'CC#BCC#BCC#BCC#B'
musicinfos = ['03:00,03:30,FOO,CC#B', '04:00,04:08,BAR,CC#BCC#BCC#B']

# m = 'ABC'
# musicinfos = ['12:00,12:14,HELLO,C#DEFGAB', '13:00,13:05,WORLD,ABCDEF']


'''
각 음은 1분에 1개씩 재생된다. 음악은 반드시 처음부터 재생되며 음악 길이보다 재생된 시간이 길 때는 음악이 끊김 없이 처음부터 반복해서 재생된다. 음악 길이보다 재생된 시간이 짧을 때는 처음부터 재생 시간만큼만 재생된다.
음악이 00:00를 넘겨서까지 재생되는 일은 없다.
조건이 일치하는 음악이 여러 개일 때에는 라디오에서 재생된 시간이 제일 긴 음악 제목을 반환한다. 재생된 시간도 같을 경우 먼저 입력된 음악 제목을 반환한다.
조건이 일치하는 음악이 없을 때에는 `(None)`을 반환한다.
'''

def change(infoinfo):
    infoinfo = infoinfo.replace('A#','H')
    infoinfo = infoinfo.replace('C#','I')
    infoinfo = infoinfo.replace('D#','J')
    infoinfo = infoinfo.replace('F#','K')
    infoinfo = infoinfo.replace('G#','L')
    return infoinfo

def solution(m, musicinfos):
    temp = {}
    # 기존 : temp에 넣는 것은 [재생된 시간, name] -> 이렇게하면 재생시간이 같을 때 먼저 들어온 애를 뽑아내려면 idx도 다시 추가해야함
    # 변경 : {}
    change_m = change(m)
    for musicinfo in musicinfos:
        start, end, name, info = musicinfo.split(',')
        change_info = change(info)
        time = (int(end[:2]) - int(start[:2])) * 60 + (int(end[3:]) - int(start[3:]))
        i, j = divmod(time, len(change_info))  # 바뀐 m, change_info로 진행해야함
        check_info = change_info * i + change_info[:j]

        if change_m in check_info:
            temp[check_info] = name


    result = None

    if len(temp) == 0:  # else문을 먼저하면 런타임에러가 뜬다
        return "(None)"
    else:
        for song in temp.keys():
            if result == None:
                result = song
            else:
                if len(result) < len(song):
                    result = song
        return temp[result]


print(solution(m, musicinfos))

# 3, 6, 7, 18 19 22 23 24 29