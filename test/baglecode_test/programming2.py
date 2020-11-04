# N = 7
# relation = [[1,2],[2,5],[2,6],[1,3],[1,4],[3,7]]
# dirname = ['root','abcd','cs','hello','etc','hello','solution']

N = 7
relation = [[1,2],[2,3],[3,4],[4,5],[1,6],[6,7]]
dirname = ['root','a','b','c','d','efghij','k']



def solution(N, relation, dirname):
    check = {}
    for a, b in relation:
        if a not in check:
            check[a] = [b]
        else:
            check[a].append(b)

    result = [[1] for _ in range(len(check[1]))]

    mymax = 0
    while result:
        r = result.pop(0)
        x = r[-1]
        print(result)
        if x in check:
            while check[x]:
                num = check[x].pop()
                r.append(num)
                result.append(r)
                break

        else:
            print('finish')
            print(r)
            answer = 0
            for val in r:
                print(type(val))
                answer += len(dirname[val - 1]) + 1

            if mymax < answer:
                mymax = answer
    print(mymax)
        # print(result)