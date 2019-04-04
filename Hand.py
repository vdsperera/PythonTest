from Deck import Deck;

class Hand(Deck):
    pass;

    def __init__(self, name = ''):
        self.cards = [];
        self.name = name;

    def add(self, card):
        self.cards.append(card);

    def __str__(self):
        s = 'Hand ' + self.name;
        if self.is_empty():
            s = s + ' is empty\n';
        else:
            s = s + " contains\n";
        return s + Deck.__str__(self);
