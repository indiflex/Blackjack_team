##플레이어 Hit/Stay 의사 입력받는 부분.
## input(Hit/sTay)


## 히트 스테이 input부분.
import Person
from Deck import share

class Player(Person):
    def isStay(self):
        user_input = input("Hit or Stay???('h' for Hit, 's' for Stay) >> ")
        if user_input == 'h':
            new_card = share()
            return self.hand.append(new_card) ## 슈퍼 써서 bust call
        else:
            print("isStay return is Player Stay")
            break
    
    