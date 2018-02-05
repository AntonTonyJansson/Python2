from collections import namedtuple

class PlayingCard:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def get_value(self):
        return self.value

    def get_suit(self):
        return self.suit

class NumberedCard(PlayingCard):
    def __init__(self, value, suit):
        super(NumberedCard, self).__init__(value, suit)

    def get_value(self):
        return super(NumberedCard, self).get_value()

    def get_suit(self):
        return super(NumberedCard, self).get_suit()

class JackCard(PlayingCard):
    def __init__(self, suit):
        super(JackCard, self).__init__(11, suit)

    def get_value(self):
        return super(JackCard, self).get_value()

    def get_suit(self):
        return super(JackCard, self).get_suit()

class QueenCard(PlayingCard):
    def __int__(self, suit):
        super(QueenCard, self).__init__(12, suit)

    def get_value(self):
        return super(QueenCard, self).get_value()

    def get_suit(self):
        return super(QueenCard, self).get_suit()

class KingCard(PlayingCard):
    def __init__(self, suit):
        super(KingCard, self).__init__(13, suit)

    def get_value(self):
        return super(KingCard, self).get_value()

    def get_suit(self):
        return super(KingCard, self).get_suit()

class AceCard(PlayingCard):
    def __init__(self, suit):
        super(AceCard, self).__init__(14, suit)

    def get_value(self):
        return super(AceCard, self).get_value()

    def get_suit(self):
        return super(AceCard, self).get_suit()

class StandardDeck:
    def __init__(self):
        self.cards = []
        suits = ['hearts', 'diamonds', 'spades', 'clubs']
        self.cards.append((14, "Hjärter"))
        #Skapa kortlek med 52 kort
    def shuffle(self):
        pass
        # Blanda kort
    def take_top(self):
        pass
        # Ta översta kortet





kort = PlayingCard(3,"hjärter")
print(kort.suit)

deck = StandardDeck()
print(deck)