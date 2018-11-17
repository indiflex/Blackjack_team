#카드 받아서 저장하는 부분. 리스트로 받는다.

import random
from Card import Card

shape = ["S", "D", "H", "C"]
number = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
point = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "10", "10", "10"]
points = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "10", "10", "10"] * 4

card = {}
for i in range(13):
    card[number[i]] = point[i] 
print(card)

y = list(card.keys())
print(y)


d_cards = []
p_cards = []

#return 받은 카드 리스트. = hand

## hand의 패수가 2장인지?

while len(d_cards) != 2:
    d_cards.append(d_cards)
    if len(d_cards) == 2:
        print ("Dealer has ", d_cards)
print()

while len(p_cards) == 2:
    p_cards.append(p_cards)
    if len(p_cards) == 2:
        print ("player has ", p_cards)
print()

## hand의 합이 21보다 크거나 같은가?
## 아니면 게임. 크거나 같으면 끄읕.

# d_hand = []
# p_hand = []

# def total():

# total = sum(d_hand)

def score(d_hand, p_hand):
	if total(p_hand) == 21:
		print(d_hand, p_hand)
		print ("You've got a Blackjack!\n")
	elif total(d_hand) == 21:
		print(d_hand, p_hand)		
		print("The dealer've got a blackjack.\n")
	elif total(p_hand) > 21:
		print(d_hand, p_hand)
		print ("Sorry. You've lost.\n")
	elif total(d_hand) > 21:
		print(d_hand, p_hand)			   
		print ("You've won.\n")
	elif total(p_hand) < total(d_hand):
		print(d_hand, p_hand)
        # print("You've lost.\n")
	else: 
		print(d_hand, p_hand)			   
		print("You've won.\n")

# ##Hit/Stay 상태를 확인하는 부분.


# ## Hit 함수 카드 받는 함수.

# h_or_s = input("Hit or Stay?>>>")
# ## Stay


