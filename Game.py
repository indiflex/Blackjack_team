## main programm
from Card import Card
import Deck
import Player
import Dealer

card = Card()   ## 카드 딕셔너리를 받는 부분
# deck = Deck()   ## 카드키값만 가지고 리스트가 오는 부분.
player = Player()   ## 인스턴스
dealer = Dealer()   ## 인스턴스

Deck.share(Deck)

if len(player.hand) <= 2 and len(dealer.hand) <= 2:
    bust(player.hand)  ## 각각 가지고 hand의 점수가 21 혹은 over되는지 확인하는 함수.
    bust(dealer.hand)

player.isStay() ## 히트지, 스테이인지 물어보는 곳.
                ## input 이 들어가서 입력을 받아야는 함수인것.
Bust(player.hand)


if player.isStay() != 0 or Bust() == 0:
    dealer.isStay() ## 히트지, 스테이인지 물어보는 곳.
                    ## input 이 들어가서 입력을 받아야는 함수인것
    

## 승패 결정. 문구 프린트.

for i in len(player.hand):
    player.point.append(card(player.hand[i]))
p_score = sum(player.point)

for i in len(dealer.hand):
    dealer.point.append(card(dealer.hand[i]))
d_score = sum(dealer.point)

if p_score > d_score:
    print(p_score, d_score)
    print ('You have won')

elif p_score == d_score:
    print(p_score, d_score)
    print ('You have tied the dealer')

elif p_score < d_score:
    print(p_score, d_score)
    print("You have lost")
