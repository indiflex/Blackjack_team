## Hit/Stay인지 판단하는 부분.
## 규칙 17이상인가?
## 이상이면 stay, 미만이면 hit

import Person

class Dealer(Person):
    def isStay():
        if self.point < 17:
            new_card = share()
            return self.hand.append(new_card)   ## 슈퍼 써서 bust call
        else:
            print("isStay return is Dealer Stay")
            break
    

