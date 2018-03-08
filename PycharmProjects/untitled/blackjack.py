import random

class BlackJack():
    def __init__(self, card):
        self.card = card
        self.hands = [self.card.pop() % 13 + 1, self.card.pop() % 13 + 1]

    def call(self):
        self.hands.append(self.card.pop() % 13 + 1)

    def calc(self):
        flag = 0
        total = 0
        for each in self.hands:
            if each == 1:
                flag = 1
            if each >= 10:
                total += 10
            else:
                total += each
        if total <= 11 and flag:
            total += 10
        return total

def main():
    card = list(range(1, 53))
    random.shuffle(card)
    player1 = BlackJack(card)
    print len(card)
    player2 = BlackJack(card)
    print len(card)
    first = 0
    calc1, calc2 = 0, 0
    while calc1 <= 21:
        player1.call()
        calc1 = player1.calc()

        if calc1 > 21:
            first = 1
    while calc2 <= 21:
        player2.call()
        calc2 = player2.calc()
        print calc2, 2
        if calc2 > 21 and not first:
            first = 2

    if calc1 <= 21 and calc1 > calc2 or calc1 <= 21 and calc2 > 21 or first == 2:
        print 'winner: player1'
    else:
        print 'winner: player2'
    print calc1, calc2

if __name__=="__main__":
    main()


