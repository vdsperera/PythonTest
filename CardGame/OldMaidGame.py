from CardGame import CardGame;
from Card import Card;
from OldMaidHand import OldMaidHand;

class OldMaidGame(CardGame):
    pass
    def play(self, names):
        #remove queen of Clubs
        self.deck.remove(Card(0, 12));

        #make a hand for each player
        self.hands = [];
        for name in names:
            self.hands.append(OldMaidHand(name));

        #deal the cards
        self.deck.deal(self.hands);
        print('---------- Cards have been dealt');
        self.print_hands();

        #remove initial matches
        matches = self.remove_all_matches();
        
    def print_hands():

    def remove_all_matches():
        count = 0;
        for hand in self.hands:
            count += hand.remove_all_matches();
        return count;
