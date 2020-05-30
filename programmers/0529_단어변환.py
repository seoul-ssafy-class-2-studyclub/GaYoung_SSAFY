def solution(begin, target, words):
    ans = 0

    if target not in words:
        return 0

    queue = [begin]

    while len(words) != 0:
        for q in queue:
            res = []
            for word in words:
                cnt = 0
                for w in range(len(word)):

                    # 같다고 하면, cnt=1일때 break를 해야해서 break포함된 것이 두칸 더 앞으로 가야함
                    # -> 중간에 stop하지 못하고 결국 끝까지 계산한 후 break
                    if q[w] != word[w]:
                        cnt += 1

                        if cnt == 2:
                            break

                if cnt == 1:
                    res.append(word)
                    words.remove(word)

        # 밑에 if문( break ) 전에 미리 더해줘야함
        ans += 1  # queue 한번 돌때, ans += 1이 되어야함
        if target in res:
            break
        else:
            queue = res
        # print해보니까 끝에 cog가 ['cog']이런식으로 나오더라.
        # 그래서 (곧 queue가 될)target이 res에 포함되어있으면 stop

    return ans


target = 'cog'
begin = 'hit'
words = ['hot', 'dot', 'dog', 'lot', 'log', 'cog']
# begin = 'hot'
# words = ['dot', 'dog', 'lot', 'log']

print(solution(begin,target,words))