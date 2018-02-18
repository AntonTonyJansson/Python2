from random import shuffle
import enum
import numpy as np
import abc

class PlayingCard(metaclass=abc.ABCMeta):
    def __init__(self, suit):
        self.suit = suit
        if not isinstance(suit, Suits):
            raise TypeError

    @abc.abstractmethod
    def get_value(self):
        pass        # Det var type raise notimplementetexception på abstracter? Måste fråga Mikael

    def get_suit(self):
        return self.suit

    @abc.abstractmethod
    def get_name(self):
        pass

    def __str__(self):
        return self.get_name() + " of " + str(self.get_suit())


class NumberedCard(PlayingCard):    # Add name to the cards
    def __init__(self, value, suit):
        self.value = value
        super().__init__(suit)

    def get_value(self):
        return self.value

    def get_name(self):
        return str(self.value)


class JackCard(PlayingCard):
    def get_value(self):
        return 11

    def get_name(self):
        return 'Jack'


class QueenCard(PlayingCard):
    def get_value(self):
        return 12

    def get_name(self):
        return 'Queen'


class KingCard(PlayingCard):
    def get_value(self):
        return 13

    def get_name(self):
        return 'King'


class AceCard(PlayingCard):
    def get_value(self):
        return 14

    def get_name(self):
        return 'Ace'


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

                self.cards.append(NumberedCard(i, color))

            self.cards.append(JackCard(color))

            self.cards.append(QueenCard(color))

            self.cards.append(KingCard(color))

            self.cards.append(AceCard(color))

    def shuffle(self):
        shuffle(self.cards)

    def take_top(self):
        top_card = self.cards.pop(0)
        return top_card


class Hand:

    def __init__(self):
        self.cards = []

    def add_card(self, card):
        self.cards.append(card)

    def remove_card(self, index):
        index.sort()
        index.reverse()
        if type(index) == list and len(index) > 0:
            if len(self.cards) - max(index) > 0:
                for i in index:
                    self.cards.pop(i)
            else:
                raise Exception("Index out of bounds exception")

    def sort_hand(self):
        self.cards.sort(key=lambda k: [k.get_suit().value, k.get_value()])

    def best_poker_hand_total(self, table_cards):
        total_cards = self.cards + table_cards
        return total_cards

    def best_poker_hand(self, kinds_of_values, table_cards):
        total_cards = self.best_poker_hand_total(table_cards)
        value_cards, list, suit_cards = create_bins_for_cards(total_cards)
        cond, best_hand = four_of_a_kind_test(list, value_cards, kinds_of_values)
        if cond:
            return best_hand
        cond, best_hand = full_house_test(list)
        if cond:
            return best_hand
        cond, best_hand = flush_test(total_cards, suit_cards, list)
        if cond:
            return best_hand
        cond, best_hand = straight_test(list)
        if cond:
            return best_hand
        cond, best_hand = three_of_a_kind_test(list, value_cards)
        if cond:
            return best_hand
        cond, best_hand = two_pairs_test(list, value_cards, kinds_of_values)
        if cond:
            return best_hand
        cond, best_hand = one_pair_test(list, value_cards, kinds_of_values)
        if cond:
            return best_hand
        cond, best_hand = high_card_test(list)
        if cond:
            return best_hand


    def __len__(self):
        return len(self.cards)


# Mycket upprensning behövs för de olika listorna så allt blir rätt värde
def four_of_a_kind_test(list, value_cards, kinds_of_values):
    if 4 in list:
        print('You got four of a kind in {}:s'.format(kinds_of_values[list.index(4)]))
        hand_rank = PokerHandType.four_of_a_kind.value
        rank_value = ((kinds_of_values[list.index(4)], value_cards[-1]))
        return True, PokerHand(hand_rank, rank_value)
    else:
        return False, None


def full_house_test(list):
    if 3 in list and 2 in list:
        temp_list = list.copy()
        temp_list.reverse()
        hand_rank = PokerHandType.full_house.value
        rank_value = ((len(temp_list)-1 - temp_list.index(3), len(temp_list)-1 - temp_list.index(2)))
        print('You got a full house with {}:s over {}:s' .format(kinds_of_values[len(temp_list)-1 - temp_list.index(3)],
                                                                 kinds_of_values[len(temp_list)-1 - temp_list.index(2)]))
        return True, PokerHand(hand_rank, rank_value)
    elif list.count(3) == 2:
        hand_rank = PokerHandType.full_house.value
        rank_value = ((len(list) - list.index(3), list.index(3)+2))
        print('den här funkar')
        print('You got a full house with {}:s over {}:s'.format(len(list)-1 - list.index(3), list.index(3)+1))
        return True, PokerHand(hand_rank, rank_value)
    else:
        return False, None


def flush_test(cards, suit_cards, list):
    if list.count(1) >= 5:
        v = []
        for suit in Suits:
            if suit_cards.count(suit) >= 5:
                for card in cards:
                    if card.get_suit() == suit:
                        v.append(card.get_value())
                print('You got a flush')
                hand_rank = PokerHandType.flush.value
                rank_value = ((suit, v[-1]))
                return True, PokerHand(hand_rank, rank_value)
            else:
                return False, None
    else:
        return False, None


def straight_test(list):             # Måste modifieras för när listan går utanför index i list
    if list.count(1) >= 5:
        i = 0
        temp_list = list.copy()
        temp_list.reverse()
        for c in temp_list:  # Starting point (high card)
            # Check if we have the value - k in the set of cards:
            if c > 0:
                found_straight = True
                for k in range(1, 5):
                    if temp_list[i+k] == 0:
                        found_straight = False
                        return False, None
                if found_straight:
                    hand_rank = PokerHandType.straight.value
                    rank_value = ((len(temp_list)+2 - i, len(temp_list)+2 - (i+1)))
                    return True, PokerHand(hand_rank, rank_value)
                i += 1
            else:
                i += 1
    else:
        return False, None


def three_of_a_kind_test(list, value_cards):
    if 3 in list:
        temp_list = list.copy()
        temp_list.reverse()
        print('You got three of a kind in {}:s'.format(kinds_of_values[len(temp_list)+2 - temp_list.index(3)]))
        hand_rank = PokerHandType.three_of_a_kind.value
        rank_value = ((len(temp_list)+2 - temp_list.index(3), value_cards[-1]))
        return True, PokerHand(hand_rank, rank_value)
    else:
        return False, None


def two_pairs_test(list, value_cards, kinds_of_values):
    if 2 in list and list.count(2) > 1:
        values = np.array(list)
        searchval = 2
        ii = np.where(values == searchval)[0]
        a = int(ii[-1])
        b = int(ii[-2])
        print('You got two pairs in {}:s over {}:s'.format(kinds_of_values[a],
                                                           kinds_of_values[b]))
        hand_rank = PokerHandType.two_pair.value
        rank_value = ((((kinds_of_values[a], kinds_of_values[b])), value_cards[-1]))
        return True, PokerHand(hand_rank, rank_value)
    else:
        return False, None


def one_pair_test(list, value_cards, kinds_of_values):
    if list.count(2) == 1:
        print('You got one pair in {}:s'.format(kinds_of_values[list.index(2)]))
        hand_rank = PokerHandType.pair.value
        rank_value = ((kinds_of_values[list.index(2)], value_cards[-1]))
        return True, PokerHand(hand_rank, rank_value)
    else:
        return False, None


def high_card_test(list):
    hand_rank = PokerHandType.high_card.value
    values = np.array(list)
    searchval = 1
    ii = np.where(values == searchval)[0]
    a = []
    if len(ii) == 2:
        for hc in range(0, 2):
            a.append(int(ii[-hc])+2)
    else:
        for hc in range(0, 5):
            a.append(int(ii[-hc])+2)
    rank_value = ((a))
    return True, PokerHand(hand_rank, rank_value)


def create_bins_for_cards(cards):
    list = [0]*13   # Detta bör vara 13?
    suit_cards = [0]*num_of_cards # Bör göras generellt
    i = 0
    value_cards = []
    for v in cards:
        list[v.get_value()-2] += 1  # Ändrade till -2 för att få det på rätt position
        suit_cards[i] = v.get_suit().value
        value_cards.append((v.get_value(), v.get_name()))
        i += 1
    value_cards.sort()
    return value_cards, list, suit_cards


class PokerHandType(enum.IntEnum):
    high_card = 0
    pair = 1
    two_pair = 2
    three_of_a_kind = 3
    straight = 4
    flush = 5
    full_house = 6
    four_of_a_kind = 7
    straight_flush = 8


class PokerHand:
    # Använder PokerHandType för PokerHand objektet
    def __init__(self, hand_rank, rank_value):
        # Value of hand
        self.hand_rank = hand_rank
        # Value of e.g. the pair
        self.rank_value = rank_value

    def __lt__(self, hand2):
        if self.hand_rank < hand2.hand_rank:
            return True
        elif self.hand_rank == hand2.hand_rank:
            if self.rank_value < hand2.rank_value:
                return True
            elif self.rank_value == hand2.rank_value:
                if self.rank_value[1] < hand2.rank_value[1]:
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False


kinds_of_values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
#game = Chicago()
deck = StandardDeck()
deck.shuffle()
num_of_cards = 2

hand1 = Hand()
hand2 = Hand()
dealer = Hand()

# Ge spelare 1 ett kort sen spelare två, tills båda har 2 kort:

top = deck.take_top()
hand1.add_card(top)
top = deck.take_top()
hand2.add_card(top)
top = deck.take_top()
hand1.add_card(top)
top = deck.take_top()
hand2.add_card(top)

print('This is player one\'s hand:')
for t in hand1.cards:
    print(str(t))

print('This is player two\'s hand:')
for t in hand2.cards:
    print(str(t))

player1 = hand1.best_poker_hand(kinds_of_values, [])
player2 = hand2.best_poker_hand(kinds_of_values, [])

print('Is player one\'s hand worse than players two\'s?')
print(player1 < player2)

# Flop:en, alltså dealern tar bort översta kortet och lägger ut 3 kort:

top = deck.take_top()
dealer.add_card(top)
dealer.remove_card([-1])
top = deck.take_top()
dealer.add_card(top)
top = deck.take_top()
dealer.add_card(top)
top = deck.take_top()
dealer.add_card(top)

for t in dealer.cards:
    print(str(t))

num_of_cards = 5
#total_cards1 = hand1.best_poker_hand_total(dealer.cards)
#total_cards2 = hand2.best_poker_hand_total(dealer.cards)

player1 = hand1.best_poker_hand(kinds_of_values, dealer.cards)
player2 = hand2.best_poker_hand(kinds_of_values, dealer.cards)


print(player1 < player2)

# Turn, alltså släng ett kort och lägg ut 4:e kortet:
num_of_cards = 6
top = deck.take_top()
dealer.add_card(top)
dealer.remove_card([-1])
top = deck.take_top()
dealer.add_card(top)

for t in dealer.cards:
    print(str(t))

player1 = hand1.best_poker_hand(kinds_of_values, dealer.cards)
player2 = hand2.best_poker_hand(kinds_of_values, dealer.cards)

print(player1 < player2)


# River, alltså släng ett kort och lägg ut 5:e kortet:

num_of_cards = 7
top = deck.take_top()
dealer.add_card(top)
dealer.remove_card([-1])
top = deck.take_top()
dealer.add_card(top)

for t in dealer.cards:
    print(str(t))

player1 = hand1.best_poker_hand(kinds_of_values, dealer.cards)
player2 = hand2.best_poker_hand(kinds_of_values, dealer.cards)

print(player1 < player2)

# cards = []
# hand3 = Hand()
# for color in Suits:
#     hand3.cards.append(JackCard(color))
# hand3.remove_card([-1])
# for color in Suits:
#     hand3.cards.append(QueenCard(color))
# hand3.remove_card([-1])
# hand3.remove_card([-1])
# for t in hand3.cards:
#     print(str(t))
#     player3 = hand3.best_poker_hand(kinds_of_values, [])
