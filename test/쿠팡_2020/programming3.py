k = 3
score = [24, 22, 20, 10, 5, 3, 2, 1]

# k = 2
# score = [1300000000,700000000,668239490,618239490,568239490,568239486,518239486,157658638,157658634,100000000,100]
diff = {}
for i in range(len(score)-1):
    key = score[i] - score[i+1]
    if key not in diff:
        diff[key] = [[i, i+1]]

    elif key in diff:
        diff[key].append([i, i+1])
print(diff)
total = len(score)
temp = []
for key, val in diff.items():
    if len(val) >= k:
        for i in val:
            for j in range(2):
                if i[j] not in temp:
                    temp.append(i[j])

print(total - len(temp))
