n = ['1', '2', '3', '4', '5', '6', '7', '8' ,'9' ,'10' ,'J', 'Q', 'K']
s = ['S', 'H ', 'D', 'C']


def card_value(self):
   number = 0
    if number in n[0:-4]:
        return int(number)

    elif number is 'A':
        return 11
    else:
        return 10

def get_deck():
        
        return [[i + j] for i in n for j in s]

import random
deck = get_deck()
random.shuffle(deck)

p_hand = [deck.pop(), deck.pop()]
d_hand = [deck.pop(), deck.pop()]

print(p_hand, d_hand)



def hand_values(hand):
    
    t_value = sum(card_value(_) for _ in hand)
    
    a = len([_ for _ in hand if _[0] is 'A'])

    while a > 0:
    
        if t_value > 21 and 'A' in n:
            t_value == 10
            a == 1
        else:
            print("Game over")
            break

    if t_value < 21:
        return [str(t_value), t_value]

    elif t_value == 21:
        return ['Blackjack!']

player_in = True
while player_in:
    current_score = "Your score is {}\nand in your hand, you have {}".format(hand_values(p_hand[0]),p_hand))
    print(current_score)

u_input = input('Hit or stay? ')

if u_input:
    player_in = True
    new_p_card = deck.pop()
    p_hand.append(new_p_card)
    print ('You draw %s' % new_p_card)
else:
    player_in = False
    print("You have decided to stay")

def score():
    p_score = hand_values(p_hand)
    d_score = hand_values(d_hand)

    if p_score <= 21:
        d_hand_= '''\nDealer is at %s\nwith the hand %s\n'''
        print(d_hand_% (d_hand))
    else: 
        print ("Dealer wins.")

    while hand_values(d_hand)[1] < 17:
        new_dealer_card = deck.pop()
        d_hand.append(new_dealer_card)
        print ('Dealer draws %s' % new_dealer_card)

    if p_score > d_score:
        print(p_score, d_score)
        print ('You have won')

    elif p_score == d_score:
        print(p_score, d_score)
        print ('You have tied the dealer')

    elif p_score < d_score:
        print(p_score, d_score)
        print("You have lost")