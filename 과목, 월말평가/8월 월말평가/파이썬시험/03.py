# 파일명 및 함수명을 변경하지 마시오.
# def summary(word):
word = 'aabbaacc'
index_1 = 0
index_2 = 0
result = []
for i in range(len(word)-1):
    if word[i] != word[i+1]:
        index_2 = i
        result.append(word[index_1:index_2+1])
        index_1 = index_2 + 1
        # if i == len(word)-1:
result.append(word[index_1:])
print(result)

    # for k in result:
    #     return '{0}{1}'.format(k, len(k)

# print(summary('aabbaacc'))
# print(summary('ffgggeeeef'))
# print(summary('abcdefg'))