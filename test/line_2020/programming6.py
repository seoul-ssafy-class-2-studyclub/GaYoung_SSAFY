def solution(companies, applicants):
    user = {}
    visit = {}
    for i in applicants:
        user_name, rank, cnt = i.split()
        user[user_name] = rank[:int(cnt)]  # {'a': 'A', 'b': 'A', 'c': 'A'}
        visit[user_name] = 0

    company = {}
    for i in companies:
        name, favor, number = i.split()  # 'A', 'abc', '2'
        company[name] = ''
        for j in favor:
            print(j)
            if name in user[j] and visit[j] == 0:
                if name not in company:
                    company[name] = j
                    visit[j] = 1
                else:
                    if len(company[name]) < int(number):
                        company[name] += j
                        visit[j] = 1

    answer = []
    for key, value in company.items():
        answer.append(key + '_' + ''.join(sorted(list(value))))
    # print(answer)

    return answer

companies = ["A fabdec 2", "B cebdfa 2", "C ecfadb 2"]
applicants = ["a BAC 1", "b BAC 3", "c BCA 2", "d ABC 3", "e BCA 3", "f ABC 2"]

# companies = ["A abc 2", "B abc 1"]
# applicants = ["a AB 1", "b AB 1", "c AB 1"]



