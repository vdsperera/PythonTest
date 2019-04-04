from Hand import Hand;
from Card import Card;

class OldMaidHand(Hand):
    pass;
    def remove_matches(self):
        count = 0;
        original_cards = self.cards[:];
        for card in original_cards:
            match = Card(3 - card.suit, card.rank);
            if match in self.cards:
                self.cards.remove(card);
                self.cards.remove(match);
                print("Hand {0}: {1} matches {2}".format(self.name, card, match));
                count += 1;
        return count;
    
