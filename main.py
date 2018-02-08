from random import shuffle
import enum


class PlayingCard:
    def get_value(self):
        return self.value

    def get_suit(self):
        return self.suit


class NumberedCard(PlayingCard):
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit


class JackCard(PlayingCard):
    def __init__(self, suit):
        self.value = 11
        self.suit = suit


class QueenCard(PlayingCard):
    def __init__(self, suit):
        self.value = 12
        self.suit = suit


class KingCard(PlayingCard):
    def __init__(self, suit):
        self.value = 13
        self.suit = suit


class AceCard(PlayingCard):
    def __init__(self, suit):
        self.value = 14
        self.suit = suit


class Suits(enum.IntEnum):
    hearts = 3
    spades = 2
    diamonds = 1
    clubs = 0


class StandardDeck:
    def __init__(self):
        self.cards = []

        suits = [Suits.hearts, Suits.diamonds, Suits.spades, Suits.clubs]

        for i in range(2, 11):
            for color in suits:
                self.cards.append((str(i), NumberedCard(i, color)))

        for color in suits:
            self.cards.append(("Jack", JackCard(color)))

        for color in suits:
            self.cards.append(("Queen", QueenCard(color)))

        for color in suits:
            self.cards.append(("King", KingCard(color)))

        for color in suits:
            self.cards.append(("Ace", AceCard(color)))

    def shuffle(self):
        shuffle(self.cards)

    def take_top(self):
        top_card = self.cards.pop(0)
        return top_card


class Hand:

    def __init__(self):
        self.hand = []

    def add_card(self, card):
        if len(self.hand) < 5:
            self.hand.append(card)
        else:
            raise Exception("Index out of bounds exception")

    def remove_card(self, index):
        index.sort()
        index.reverse()
        if len(self.hand) - max(index) > 0:
            for i in index:
                self.hand.pop(i)
        else:
            raise Exception("Index out of bounds exception")

    def sort_hand(self):
        self.hand.sort(key=lambda k: [k[1].get_suit().value, k[1].get_value()])


class PokerHand(enum.IntEnum):
    pair = 1
    two_pair = 2
    # etc...

class Pair(PokerHand):
    pass

deck = StandardDeck()
deck.shuffle()
print(len(deck.cards))
for t in deck.cards:
    print(t[0], " of ", t[1].get_suit().name)
#print(deck.cards[1][1].get_value()

#if deck.cards[0][1].get_value() == deck.cards[1][1].get_value():
#    if deck.cards[0][1].get_suit().value > deck.cards[1][1].get_suit().value:
#        print(deck.cards[0][1].get_suit().name)
#    else:
#        print(deck.cards[1][1].get_suit().name)

#print(deck.cards[0][1].get_value())

top = deck.take_top()
print("Top card: ", top)
for t in deck.cards:
    print(t[0], " of ", t[1].get_suit().name)

print(len(deck.cards))

hand = Hand()
hand.add_card(top)
top = deck.take_top()
hand.add_card(top)
top = deck.take_top()
hand.add_card(top)

for t in hand.hand:
    print(t[0], " of ", t[1].get_suit().name)

hand.sort_hand()

for t in hand.hand:
    print(t[0], " of ", t[1].get_suit().name)

index = [2, 3]
print("Print max index: ", max(index))
hand.remove_card(index)

for t in hand.hand:
    print(t[0], " of ", t[1].get_suit().name)
