## class card에서 만든 카드를 받아서 셔플하는 부분.
## return 셔플된 카드 리스트.
## 카드는 리스트로 해서 일단 오는 것으로 가정.
import random
#from Card import card


def card_shuffle():
    random.shuffle(card)
    # print("card_shuffle = ", card)
    return list(card)

## 카드를 분배하는 곳.
def card_give(list):
    card = card_shuffle()
    return card.pop()
        

# card_shuffle()


# for i in range(6):
#     a = card_give
#     print("card_give = ", card_give(card_shuffle))
# print("=======> card_shuffle = ", card_shuffle())

card = [1,2,3,4,5]
print("card = ", card)
a = card_give(card)
print("card_give = ", a)
print("card = ", card)
a = card_give(a)
print("card_give = ", a)
print("card = ", card)
a = card_give(a)
print("card_give = ", a)
print("card = ", card)
a = card_give(a)
print("card_give = ", a)
print("card = ", card)
