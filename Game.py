## main programm

card = Card()   ## 카드 딕셔너리를 받는 부분
deck = Deck()   ## 카드키값만 가지고 리스트가 오는 부분.
player = Player()   ## 인스턴스
dealer = Dealer()   ## 인스턴스

    
if len(player.hand) <= 2 and len(dealer.hand) <=2:
    share()
    Bust(player.hand)  ## 각각 가지고 hand의 점수가 21 혹은 over되는지 확인하는 함수.
    Bust(Dealer.hand)

player.isStay() ## 히트지, 스테이인지 물어보는 곳.
                ## input 이 들어가서 입력을 받아야는 함수인것.
Bust(player.hand)






if player.isStay() != 0 or Bust() == 0
    dealer.isStay() ## 히트지, 스테이인지 물어보는 곳.
                ## input 이 들어가서 입력을 받아야는 함수인것
    

score() ## 승패 결정. 문구 프린트하는 함수.


