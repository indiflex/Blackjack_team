from random import shuffle


def card():
    pattern = ['S', 'C', 'H', 'D']
    numbers = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    point = ['2', '3', '4', '5', '6', '7', '8', '9', '10', '10', '10', '10', '11'] * 4
    card_form = list()
    card_set = dict()
    for i, j in enumerate(pattern):
        for v, w in enumerate(numbers):
            card_form.append(j + w)
    for x in range(52):
        card_set[card_form[x]] = point[x]
    return card_set


def deck_key():
    deck_card = dict()
    deck_keys = list()
    deck_card = card()
    deck_keys = list(deck_card.keys())
    shuffle(deck_keys)
    return deck_keys


def deck_share(x):
    return x.pop()


def give_2cards(x, y, z):
    for i in range(2):
        x.append(deck_share(z))
        y.append(deck_share(z))
    if y[0] <= y[1]:
        print("Dealer's hand = {}".format(y[0]))
    else:
        print("Dealer's hand = {}".format(y[1]))


def outcome(x, y):
    print("..............Dealer's score =", y)
    if x < 21 and y < 21:
        if x == y:
            print("Draw!!!")
        elif x > y:
            print("Player win the game!")   
        else:
            print("Player lost the game!")
    elif x == 21:
        print("Player win the game!")
    elif y == 21:
        print("Player lost the game!")
    elif x < 21 and y > 21:
        print("Player win the game!")
    elif x > 21 and y < 21:
        print("Player lost the game!")
    else:
        pass


def close_game(y):
    user_input = input("Wanna continue the game??\nPress 'r' to resume the game or 'q' to quit >>> ")
    if user_input == 'r':    
        return True
    elif user_input == 'q':
        print("THANK YOU FOR YOUR PLAYING!!!")
        exit()
    else:
        print("Please check your Key!") ##2  키 재입력 받는 방법??
        return close_game(y)
    