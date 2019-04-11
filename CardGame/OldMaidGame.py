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
        print("---------- Matches discarded, play begins")
        self.print_hands()

        #play until all 50 cards are matched
        turn = 0;
        numHands = len(self.hands)
        while matches < 25:
            matches += self.play_one_turn(turn)
            turn = (turn + 1) % numHands
        
        print("---------- Game is Over")
        self.print_hands()
        
    def print_hands(self):
        for hand in self.hands:
            print(hand)

    def remove_all_matches(self):
        count = 0;
        for hand in self.hands:
            count = count + hand.remove_matches();
        return count;

    def play_one_turn(self, i):
        if self.hands[i].is_empty():
            return 0
        neighbor = self.find_neighbor(i)
        pickedCard = self.hands[neighbor].pop_card()
        self.hands[i].add(pickedCard)
        print("Hand", self.hands[i].name, "picked", pickedCard)
        count = self.hands[i].remove_matches()
        self.hands[i].shuffle()
        return count        

    def find_neighbor(self, i):
        numHands = len(self.hands)
        for next in range(1,numHands):
            neighbor = (i + next) % numHands
            if not self.hands[neighbor].is_empty():
                return neighbor       
