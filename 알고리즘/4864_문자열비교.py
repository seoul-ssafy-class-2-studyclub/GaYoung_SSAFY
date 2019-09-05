def standard_method(str1, str2):
    i = 0  # str1의 인덱스
    j = 0  # str2의 인덱스

    while i < len(str1) and j < len(str2):
        if str2[j] != str1[i]:
            j -= i 
            i = -1
        
        i += 1
        j += 1
    if i == len(str1):
        return 1
    else:
        return 0

for t in range(int(input())):
    str1 = input()
    str2 = input()
    print('#{} {}'.format(t+1, standard_method(str1, str2)))
