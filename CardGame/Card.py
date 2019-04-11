class Card:
    SUITS = ('Clubs', 'Diamonds', 'Hearts', 'Spades');
    RANKS = ('narf', 'Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King');
    
    def __init__(self, suit = 0, rank = 0):
        self.suit = suit;
        self.rank = rank;

    def __str__(self):
        """
          >>> print(Card(2, 11))
          Jack of Hearts
        """        
        return '{0} of {1}'.format(Card.RANKS[self.rank], Card.SUITS[self.suit]);

    def __cpm__(self, other):
        if self.suit > other.suit:
            return 1;
        if self.suit < other.suit:
            return -1;
        if self.rank > other.rank:
            return 1;
        if self.rank < other.rank:
            return -1;
        return 0;
        

if __name__ == '__main__':
    import doctest
    doctest.testmod()
