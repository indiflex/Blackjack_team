## class card에서 만든 카드를 받아서 셔플하는 부분.
## return 셔플된 카드 리스트.
## 카드는 리스트로 해서 일단 오는 것으로 가정.
import random
from Card import Card

# false_data = {"S2" : 2, "S3" : 3, "S4" : 4, "S5" : 5, "S6" : 6}

# def pop(self):
#     false_data = {"S2" : 2, "S3" : 3, "S4" : 4, "S5" : 5, "S6" : 6}
#     x = list(false_data.keys())
#     random.shuffle(x)

# popx = x.pop()
# print(popx)


# print(x)

# print(x.pop())
# print(x)
# print(x.pop())
# print(x)
# print(x.pop())
# print(x)
# print(popx)
# dic = []
# print(dic.append(popx))
# a = dic.append(popx)

class Deck():
    def __init__(self):
        self.key = []
        y = list(cards.keys())
        random.shuffle(y)
        print(y)
        return y

# x는 카드키값 리스트
    def share(self.key):
        y = list(x.keys())
        return y.pop()

exit()
