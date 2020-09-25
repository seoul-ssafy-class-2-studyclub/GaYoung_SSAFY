def solution(histogram):
    answer = 12
    return answer

histogram = [2, 2, 2, 3]
# histogram = [6, 5, 7, 3, 4, 2]

mymax = 0
for i in range(len(histogram)):
    for j in range(i+2, len(histogram)):
        if histogram[i] > 0 and histogram[j] > 0:
            water = (j - i - 1) * min(histogram[i], histogram[j])

            if mymax < water:
                mymax = water

print(mymax)