def solution(heights):
    h = len(heights)
    ans = [0] * h
    for i in range(h - 1, 0, -1):
        for j in range(i - 1, -1, -1):
            if heights[i] < heights[j]:
                ans[i] = j + 1
                break

    return ans