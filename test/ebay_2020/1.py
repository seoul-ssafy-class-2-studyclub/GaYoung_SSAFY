'''
1번

## 입력 처리
도착 시간 + 상담 시간 = 종료시간

## 종료 시간 지난 아이템 제거
Set의 원소중에서, 도착시간보다 작은 값이 있다면 제거(iterator)

## 상담 받을 수 있는지 체크
Set 사이즈가 N보다 작을 시에 상담가능
- 종료시간 Set에 넣어주기
Set 사이즈가 N과 같을 시에 상담불가
- 도착 시간 + (도착시간 - Set 자료구조의 가장 최소값 = 최소 대기시간)으로 변경
- 정답에 최소 대기시간 더하고 재검사

'''

N = 2
simulation_data = [[0, 3], [2, 5], [4, 2], [5, 3]]

time = 0
check = []
while True:
    for simulation in simulation_data:
        stay, consult = simulation
        if stay == time and len(check) < N:
            check.append([stay, 1])
            break

        elif stay != time:
            for i in check:
                ss, up = i
                up += 1

                if consult == up:
                    check.pop()



    time += 1
    print(check)
    if check == []:
        break