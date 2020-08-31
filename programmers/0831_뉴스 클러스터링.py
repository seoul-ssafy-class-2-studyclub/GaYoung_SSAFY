def solution(str1, str2):

    def make_split(word):

        answer = []
        for i in range(len(word) - 1):
            w = word[i:i + 2]
            if w.isalpha():
                answer.append(w)

        return answer

    def make_interection(one, two):
        answer = []
        for i in range(len(one)):
            for j in range(len(two)):
                if one[i] == two[j]:
                    answer.append(one[i])
                    del two[j]
                    break


        return answer

    str1 = str1.upper()
    str2 = str2.upper()

    one = make_split(str1)
    two = make_split(str2)
    len_one = len(one)
    len_two = len(two)
    print(one)
    print(two)

    if len_one == 0 and len_two == 0:
        return 65536

    elif one == two:
        return 65536


    else:  # union, intersection 쓸 수 없는 이유 -> set은 중복된 것을 지운다
           # one = ['AA', 'AA'], two = ['AA', 'AA', 'AA']이면 make_split에서 set로 두면 one = two = {'AA'}로 나온다
        part = make_interection(one, two)
        print(part)
        total = len_one + len_two - len(part)
        # print(total)
        result = len(part) / total * 65536
        print(result)

        return int(result)

str1 = 'FRANCE'
str2 = 'french'

# str1 = 'handshake'
# str2 = 'shake hands'

# str1 = 'aa1+aa2'
# str2 = 'AAAA12'

# str1 = 'E=M*C^2'
# str2 = 'e=m*c^2'

print(solution(str1, str2))

'''
1. one, two를 대문자로 통일한 후, 합집합, 교집합을 구한다.
  ** 문제점 : union, interaction은 set일 때 사용가능
        - set하게 되면 만약, one = ['AA', 'AA'], two = ['AA', 'AA', 'AA']라면 
          set_one = set_two = {'AA'}로 동일해진다
  ** 해결책 : 
        - Counter함수 사용해서 union, interaction를 사용한다.
        - make_interaction함수를 만들어 교집합만 구하면 one, two, interaction(one, two)갯수로 합집합을 구한다.
'''