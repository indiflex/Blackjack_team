class Card:
    def card(self):
        
        shape = ["S", "D", "H", "C"]
        number = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
        point = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "10", "10", "10", "11"]
        points = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "10", "10", "10", "11"] * 4

        # S2 , 2 

        ### 카드를 만드는 부분. 그 값은 리스트의 형태로 반환.
        ### return card자료형... 리스트
        # {number :point}
        # { } 13개

        # card = {}
        # card = {number : point}
        # print(card)

        card = {}
        for i in range(13):
            card[number[i]] = point[i]  ## card = { num[i] : point}
                                        ## 딕셔너리 쌍 추가하기 http://mystyle1057.tistory.com/211

        # print(card)

        y = list(card.keys())
        print(y)

        score = []
        for i, j in enumerate(shape):
            for v, w in enumerate(number):
                a = j + w
                score.append(a)

        print(score)
        cards = {}
        for i in range(52):
            cards[score[i]] = points[i]                  

        # print(cards)

        return cards

        return cards


### 카드 점수 모아서 보여주는 함수.
카드 = Card()
카드.card()
