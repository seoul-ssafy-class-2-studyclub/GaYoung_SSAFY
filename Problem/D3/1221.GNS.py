number = {
    'ZRO': 0, 'ONE': 1, 'TWO': 2, 'THR': 3, 'FOR': 4,
    'FIV': 5, 'SIX': 6, 'SVN': 7, 'EGT': 8, 'NIN': 9,
}

for t in range(int(input())):
    tc, N = input().split()
    data = input().split()  # ['TWO', 'NIN', 'TWO', 'TWO', 'FIV', 'FOR']
    result = sorted(data, key=lambda x: number[x])
    print('#{0}\n{1}'.format(t+1, ''.join(result)))
