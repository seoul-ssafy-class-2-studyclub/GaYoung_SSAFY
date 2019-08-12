# max 함수
def my_max(x):
    my_value = x[0]
    for num in x:
        if my_value < num:
            my_value = num
    return my_value

for t in range(int(input())):
    n = int(input())
    data = list(map(int,list(input())))
    data_list = [0] * 10
    for i in data:
        data_list[i] += 1
    for k in range(len(data_list)-1, -1, -1):
        if my_max(data_list) == data_list[k]:
            result = k
            break
            
    print('#{0} {1} {2}'.format(t+1, result, my_max(data_list)))
    