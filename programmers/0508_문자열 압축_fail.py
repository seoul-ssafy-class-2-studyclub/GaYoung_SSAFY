def solution(s):
    if len(s) == 1:
        return 1

    ans = 999999999999999999999999999999

    for i in range(1, len(s)):
        string = ''
        cnt = 1
        for j in range(i, len(s), i):
            if s[j-i:j] == s[j:j+i]:
                cnt += 1
            else:
                if cnt == 1:
                    string += s[j-i:j]
                else:
                    string += str(cnt) + s[j-i:j]
                    cnt = 1

        if cnt > 1:
            string += str(cnt) + s[j - i:j]
        print(i, j, cnt, string)

        if ans > len(string):
            ans = len(string)

    return ans



s = "aabbaccc"
res = solution(s)
print(res)