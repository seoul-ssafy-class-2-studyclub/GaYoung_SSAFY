cards = [12, 7, 11, 6, 2, 12]
# cards = [1, 4, 10, 6, 9, 1, 8, 13]
# cards = [10, 13, 10, 1, 2, 3, 4, 5, 6, 2]
# cards = [3, 3, 3, 3, 3, 3, 3, 3, 3, 3]

def solution(cards):
    answer = -1
    return answer

for i in range(len(cards)):
    if cards[i] > 10:
        cards[i] = 10

player = [cards[0], cards[2]]  # [10, 10]
dealer = [(cards[1], 0), (cards[3], 1)]  # [7, 6]
# for i in dealer:
#     if i[1] == 1:
