a, b = list(map(int, input().split()))

def rsp(a, b):
    if (a == 1 and b == 3) or (a == 3 and b == 2) or (a == 2 and b == 1):
        print('A')
    elif (a == 3 and b == 1) or (a == 2 and b == 3) or (a == 1 and b == 2):
        print('B')
        
rsp(a, b)