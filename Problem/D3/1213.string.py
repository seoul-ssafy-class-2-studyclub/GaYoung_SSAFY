def bm_algo(pattern, text):
    t = len(text)
    p = len(pattern)

    text_index = p - 1
    pattern_index = p - 1
    count = 0

    while text_index < t:
        if text[text_index] == pattern[pattern_index]:
            if pattern_index == 0:
                count += 1
                text_index = text_index + p + 1
                pattern_index = p - 1
            else:
                text_index -= 1
                pattern_index -= 1

        else:
            while pattern_index >= 0:
                if text[text_index] == pattern[pattern_index]:
                    text_index = text_index + p - (pattern_index + 1)
                    pattern_index = p - 1
                    break
                else:
                    pattern_index -= 1

            if pattern_index == -1:
                text_index = text_index + p
                pattern_index = p - 1

    return count

for t in range(int(input())):
    N = int(input())
    pattern = input()
    text = input()
    result = bm_algo(pattern, text)
    print('#%d %d' % (t + 1, result))