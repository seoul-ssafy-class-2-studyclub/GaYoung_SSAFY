def solution(cookie):
    mymax = 0
    for m in range(len(cookie) - 1):  # i가 first와 second를 구분할 기준점
        first_ind, first_cookie = m, cookie[m]
        second_ind, second_cookie = m + 1, cookie[m + 1]

        while True:
            if first_cookie == second_cookie and first_cookie > mymax:
                mymax = first_cookie
            # first_cooke와 second_cookie가 같아도 더 나아갔을 때 큰 값이 같아질 수 있다.
            elif first_cookie <= second_cookie and first_ind > 0:
                first_ind -= 1
                first_cookie += cookie[first_ind]
            elif first_cookie >= second_cookie and second_ind < len(cookie) - 1:
                # 여기서 1이 더해지니까 second_cookie에 더해져야하는 값은 cookie[len(cookie)-1]값이다.
                second_ind += 1
                second_cookie += cookie[second_ind]
            else:
                break

    return mymax


# cookie = [1,1,2,3]  # result = 3
# cookie = [1,2,4,5]  # result = 0
cookie = [1,3,4,1,6,5]

mymax = 0
for m in range(len(cookie)-1):  # i가 first와 second를 구분할 기준점
    first_ind, first_cookie = m, cookie[m]
    second_ind, second_cookie = m+1, cookie[m+1]

    while True:
        if first_cookie == second_cookie and first_cookie > mymax:
            mymax = first_cookie
        if first_cookie <= second_cookie and first_ind > 0:
            first_ind -= 1
            first_cookie += cookie[first_ind]
        elif first_cookie >= second_cookie and second_ind < len(cookie)-1:
            # 여기서 1이 더해지니까 second_cookie에 더해져야하는 값은 cookie[len(cookie)-1]값이다.
            second_ind += 1
            second_cookie += cookie[second_ind]
        else:
            break
        print('first_ind, first_cookie')
        print(first_ind, first_cookie)
        print('second_ind, second_cookie')
        print(second_ind, second_cookie)

    print('mymax')
    print(mymax)












