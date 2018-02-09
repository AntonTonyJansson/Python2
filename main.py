from random import shuffle
import enum


class PlayingCard:
    def __init__(self, suit, name):
        self.suit = suit
        self.name = name
        if not isinstance(suit, Suits):
            raise TypeError

    def get_value(self):
        pass

    def get_suit(self):
        pass

    def get_name(self):
        return self.name

    def print(self):
        print(self.get_name(), " of ", self.get_suit())


class NumberedCard(PlayingCard):    # Add name to the cards
    def __init__(self, value, suit, name):
        self.value = value
        super().__init__(suit, name)

    def get_value(self):
        return self.value

    def get_suit(self):
        return self.suit


class JackCard(PlayingCard):
    def get_value(self):
        return 11

    def get_suit(self):
        return self.suit


class QueenCard(PlayingCard):
    def get_value(self):
        return 12

    def get_suit(self):
        return self.suit


class KingCard(PlayingCard):
    def get_value(self):
        return 13

    def get_suit(self):
        return self.suit


class AceCard(PlayingCard):
    def get_value(self):
        return 14

    def get_suit(self):
        return self.suit


class Suits(enum.IntEnum):
    hearts = 3
    spades = 2
    diamonds = 1
    clubs = 0

    def __str__(self):
        return '♣♦♠♥'[self.value]


class StandardDeck:
    def __init__(self):
        self.cards = []

        for color in Suits:
            for i in range(2, 11):

                self.cards.append(NumberedCard(i, color, str(i)))

            self.cards.append(JackCard(color, "Jack"))

            self.cards.append(QueenCard(color, "Queen"))

            self.cards.append(KingCard(color, "King"))

            self.cards.append(AceCard(color, "Ace"))

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
        self.hand.sort(key=lambda k: [k.get_suit().value, k.get_value()])

    def best_poker_hand(self, cards=[]):
        hand = self.two_pair()
        return hand

    def two_pair(self):
        list = [0]*14
        print(list)
        for v in self.hand:
            list[v[1].get_value()-1] += 1
        if 2 in list:
            print(list)

            return ((PokerHand.pair.value, PokerHand.value.value))
        else:
            return False


class PokerHandType(enum.IntEnum):
    value = 0
    pair = 1
    two_pair = 2
    # etc...


class PokerHand:
    # Använder PokerHandType för PokerHand objektet
    pass


deck = StandardDeck()
deck.shuffle()
#print(len(deck.cards))
#for t in deck.cards:
#    t.print()


#print(deck.cards[1][1].get_value()

#if deck.cards[0][1].get_value() == deck.cards[1][1].get_value():
#    if deck.cards[0][1].get_suit().value > deck.cards[1][1].get_suit().value:
#        print(deck.cards[0][1].get_suit().name)
#    else:
#        print(deck.cards[1][1].get_suit().name)

#print(deck.cards[0][1].get_value())

top = deck.take_top()
#print("Top card:", end=" ")
#top.print()
#for t in deck.cards:
#    t.print()

#print(len(deck.cards))

hand = Hand()
hand.add_card(top)
top = deck.take_top()
hand.add_card(top)
top = deck.take_top()
hand.add_card(top)

#for t in hand.hand:
#    t.print()

hand.sort_hand()

for t in hand.hand:
    t.print()

index = [2, 0]
#print("Print max index: ", max(index))
hand.remove_card(index)

for t in hand.hand:
    t.print()


#print(hand.hand)
#ret = hand.best_poker_hand()
#print(ret)