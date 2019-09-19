for t in range(int(input())):
   N = int(input())
   data = list(map(int, input().split()))
   earn = 0
   while len(data) != 0:
       idx_1 = 0
       mymax = max(data)
       idx_2 = data.index(mymax)
       buy = data[:idx_2]
       earn += mymax * len(buy) - sum(buy)
       del data[:idx_2+1]
   print('#{} {}'.format(t + 1, earn))