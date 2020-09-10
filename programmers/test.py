def solution(lines):
    answer = 0
    data = []
    for line in lines:
        line = line.split()
        end = list(map(int,line[1].replace('.',':').split(':')))
        start = float(line[2].replace('s',''))
        end = end[0]*3600000 + end[1] * 60000 + end[2] *1000 + end[3]
        start = end - int(start*1000) + 1
        data.append([start, end])
    n = len(data)
    for st, ed in data:
        sts, eds = 0,0
        for nst, ned in data:
            if st <= nst < st+1000 or st <= ned < st+1000 or (st > nst and st+1000 < ned):
                sts += 1
            if ed <= nst < ed+1000 or ed <= ned < ed+1000 or (ed > nst and ed+1000 < ned):
                eds += 1
        answer = max(answer, sts, eds)
    return answer