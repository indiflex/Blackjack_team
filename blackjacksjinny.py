class Card:
    def __init__(self):
        self.name = "카드"

    def card(self):
        import random
        s = ["Spade", "Diamond", "Heart", "Clover"]
        n = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
        i = random.choice(s)
        j = random.choice(n)
        card = i + j
        print("Your card is", card)
    
class Person(Card):
    def __init__(self):
        self.name = "사용자"
    def sum(self, x, y):
        return x + y

    class Dealer(Person):
        name = "딜러"
        

    class Player(Person):
        name = "플레이어"


카드 = Card()
카드.card()




       
    # class Deck(Card):
    #     def __init__(self, s, n):
    #         self.s = "모양"
    #         self.n = "숫자"

#     hos = input("Hit or stay? >>>")

#     def deck(self):
#         if card == hit:
#             card.join(list(card))


# class Person:
#     def __init__(self):
#         self.name = "사용자"
#     def sum(self, x, y):
#         return sum += x + y


# class Dealer(Person):
#     name = "딜러"

# class Player(Person):
#     name = "플레이어"

# 딜러 = Dealer
# 플레이어 = Player

# for x, y in list:

# if sum == 21:
#     print("Jackpot!!")
#     break

# if sum > 21:
#     print("Game over")
#     break

# else:
#     while True:
#         print("Compare each sum")
#         if sum.Dealer > sum.Player:
#             print("Dealer win!")
#         else:
#             print("Player win!")