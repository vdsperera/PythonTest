from Card import Card;

class Deck:
    def __init__(self):
        self.cards = [];
        for suit in range(4):
            for rank in range(1, 14):
                self.cards.append(Card(suit, rank));

    def print_deck(self):
        for card in self.cards:
            print(card);

    def __string__(self):
        s = "";
        for i in range(len(self.cards)):
            s += " " * i + str(self.cards[i]) + "\n";
        return s;
        

