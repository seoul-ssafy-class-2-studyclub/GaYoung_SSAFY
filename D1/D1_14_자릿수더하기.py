num = 6789
num_list = [i for i in str(num)]

total = 0

for k in num_list: # print(k) = 6 7 8 9 
    total += int(k)
print(total)