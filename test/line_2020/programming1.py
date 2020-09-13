def solution(boxes):
    check = {}
    n = len(boxes)

    for box in boxes:
        for i in box:
            if i not in check:
                check[i] = 1
            else:
                check[i] += 1

    for key, value in check.items():
        i, j = divmod(value, 2)
        if j == 0:
            n -= (j + 1)

    # print(n)

    return n

# boxes = [[1, 2], [2, 1], [3, 3], [4, 5], [5, 6], [7, 8]]
# boxes = [[1, 2], [3, 4], [5, 6]]
boxes = [[1, 2], [2, 3], [3, 1], [1, 4], [5, 6]]
