def my_set(data):
    for i in data:
        if 






for t in range(int(input())):
    str1 = input()
    str2 = input()
    str1_set = set(str1)
    result = {}
    for i in str1_set:
        result[i] = 0
        for j in list(''.join(str2)): 
            if j in i:
                result[i] += 1
    
    print('#%d' % (t+1), end=' ')
    data = []
    for k in result.values():
        data += [k]
    print('%d' % (max(data)))
        