row, col = map(int, input().split())
data = []
for i in range(int(input())):
    data.append(list(map(int, input().split())))

r_list = []
c_list = []
for k in data:
    if k[0] == 0:
        r_list += [k[1]]
    else:
        c_list += [k[1]]
r_list += [col]
c_list += [row]

r_s = sorted(r_list)
c_s = sorted(c_list)

r_result = r_s[0]
for r in range(1, len(r_s)):
    if r_result < r_s[r] - r_s[r - 1]:
        r_result = r_s[r] - r_s[r - 1]

c_result = c_s[0]
for c in range(1, len(c_s)):
    if c_result < c_s[c] - c_s[c - 1]:
        c_result = c_s[c] - c_s[c - 1]

print(r_result * c_result)