# 1. while result = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]까지 돌린다. -> len()==10까지
# 2. set() -> 반복되는 것 없애기
# 
# 




# T = int(input())
# for t in range(1, T + 1):
result = {}  # set
for i in range(1, 100):
    a = int(input())  # 1259
    N = a * i
    N_list = {int(n) for n in str(N)}   # [1, 5, 9, 6]
    result.update(N_list)   # {1, 5, 6, 9}
    print(result)



        # i += 1
    
# print(len(a))
 