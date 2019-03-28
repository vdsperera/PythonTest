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

    def __str__(self):
        s = ""
        for i in range(len(self.cards)):
            s += " " * i + str(self.cards[i]) + "\n"
        return s

    def shuffle(self):
        import random;
        num_cards = len(self.cards);
        for i in range(num_cards):
            j = random.randrange(i, num_cards);
            self.cards[i], self.cards[j] = self.cards[j], self.cards[i];

    def remove(self, card):
        if card in self.cards:
            self.cards.remove(card);
            return true;
        else:
            return false;

    def pop(self):
        return self.cards.pop();

    def is_empty(self):
        return (len(self.card) == 0);
            
        

