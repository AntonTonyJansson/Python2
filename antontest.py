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
        else:
            print('No card chosen to discard')

    def sort_hand(self):
        self.cards.sort(key=lambda k: [k.get_suit().value, k.get_value()])

    def best_poker_hand2(self, table_cards=[]):
        total_cards = self.cards + table_cards      # Kan modifieras in så att spelet funkar för texad holdem

    def best_poker_hand(self, kinds_of_values):     # Just nu funkar detta bara för chicago inte för texas
        value_cards, list, suit_cards = create_bins_for_cards(self.cards)
        if 4 in list:
            print('You got four of a kind in {}:s' .format(kinds_of_values[list.index(4)]))
            hand_rank = PokerHandType.four_of_a_kind.value
            rank_value = ((kinds_of_values[list.index(4)], value_cards[-1]))
            return PokerHand(hand_rank, rank_value)
        elif 3 in list and 2 in list:
            hand_rank = PokerHandType.full_house.value
            rank_value = ((list.index(3), len(list) - list.reverse().index(2)))
            return PokerHand(hand_rank, rank_value)
        elif list.count(3) == 2:
            hand_rank = PokerHandType.full_house.value
            rank_value = ((len(list) - list.reverse().index(3), list.index(3)))
            return PokerHand(hand_rank, rank_value)
        elif list.count(1) >= 5:
            for suit in Suits:
                if suit_cards.count(suit) >= 5:
                    print('You got a flush')
                    hand_rank = PokerHandType.flush.value
                    rank_value = ((suit, ))
                    return PokerHand(hand_rank, rank_value)
            first_pos = list.index(1)
            second_pos = first_pos+1
            subseq_cards = 0
            while list[second_pos] == list[first_pos] and second_pos < 15:
                print(first_pos+2, 'and ', second_pos+2, 'are subsequent')
                first_pos += 1
                second_pos += 1
                subseq_cards += 1
            if subseq_cards == 4:
                hand_rank = PokerHandType.straight.value
                highest_card = value_cards[-1]
                rank_value = 0  # ÄNDRA!
                return PokerHand(hand_rank, highest_card, rank_value)
            else:
                hand_rank = PokerHandType.value.value
                highest_card = value_cards[-1]
                return PokerHand(hand_rank, highest_card, 0)
        elif 3 in list:
            print('You got three of a kind in {}:s' .format(kinds_of_values[list.index(3)]))
            hand_rank = PokerHandType.three_of_a_kind.value
            highest_card = value_cards[-1]
            rank_value = kinds_of_values[list.index(3)]
            return PokerHand(hand_rank, highest_card, rank_value)
        elif 2 in list:
            if list.count(2) > 1:
                values = np.array(list)
                searchval = 2
                ii = np.where(values == searchval)[0]
                a = int(ii[-1])
                b = int(ii[-2])
                print('You got two pairs in {}:s over {}:s' .format(kinds_of_values[a], kinds_of_values[b]))
                hand_rank = PokerHandType.two_pair.value
                highest_card = value_cards[-1]
                rank_value = kinds_of_values[a], kinds_of_values[b]
                return PokerHand(hand_rank, highest_card, rank_value)
            else:
                print('You got one pair in {}:s' .format(kinds_of_values[list.index(2)]))
                hand_rank = PokerHandType.pair.value
                highest_card = value_cards[-1]
                rank_value = kinds_of_values[list.index(2)]
                return PokerHand(hand_rank, highest_card, rank_value)

    def __len__(self):
        return len(self.cards)


def create_bins_for_cards(cards):
    list = [0]*13   # Detta bör vara 13?
    suit_cards = [0]*5 # Bör göras generellt
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
    value = 0
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
        if self.hand_rank > hand2.hand_rank:
            return True
        elif self.rank_value > hand2.rank_value:
            return True
        elif self.rank_value[1] > hand2.rank_value[1]:
            return True
        else:
            return False


class Game:
    def __init__(self):
        self.kinds_of_values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']

    @abc.abstractmethod
    def start_game(self):
        pass

    @abc.abstractmethod
    def run_game(self):
        pass

    @abc.abstractmethod
    def show_game_state(self, rounds):
        pass


class Chicago(Game):
    def __init__(self):
        super().__init__()
        self.max_num_of_cards = 5
        self.hand = Hand()
        self.num_of_rounds = 3
        self.max_num_of_cards_to_swap = 5

    def start_game(self):
        deck = StandardDeck()
        deck.shuffle()
        while len(self.hand) < self.max_num_of_cards:
            top = deck.take_top()
            self.hand.add_card(top)
        return deck, self.hand

    def run_game(self):
        for rounds in range(self.num_of_rounds):
            self.show_game_state(rounds)
            discarded_cards = '[' + input('Select cards to discard by giving the index from 0 to {} separated by commas'
                                          ' or press \'Enter\' \n' .format(self.max_num_of_cards_to_swap-1)) + ']'
            discarded_cards = eval(discarded_cards)
            self.hand.remove_card(discarded_cards)
            while self.hand.__len__() < self.max_num_of_cards:
                top = deck.take_top()
                self.hand.add_card(top)

    def show_game_state(self, rounds):
        self.hand.sort_hand()
        print('This is your hand, sorted by color and then value:')
        for t in self.hand.cards:
            print(str(t))
        current_hand = self.hand.best_poker_hand(self.kinds_of_values)
        hand_value, hand_high_card = current_hand.hand_rank, current_hand.highest_card
        vowels = 'A8'
        if hand_high_card[1][0] in vowels:
            article = ', an'
        else:
            article = ', a'
        print('The hand\'s value is:', hand_value)
        print('Highest card is: {}{} {}' .format(hand_high_card[0], article, hand_high_card[1]))
        if rounds <= self.num_of_rounds:
            print('This is swap number:', rounds + 1, 'out of', self.num_of_rounds)


kinds_of_values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
game = Chicago()
deck = StandardDeck()
deck.shuffle()

hand1 = Hand()
while len(hand1) < 5:
    top = deck.take_top()
    hand1.add_card(top)
for t in hand1.cards:
    print(str(t))
discarded_cards = '[' + input('Select cards to discard by giving the index from 0 to {} separated by commas'
                              ' or press \'Enter\' \n'.format(5 - 1)) + ']'
discarded_cards = eval(discarded_cards)
hand1.remove_card(discarded_cards)
player1 = Hand.best_poker_hand(hand1, kinds_of_values)




hand2 = Hand()
while len(hand2) < 5:
    top = deck.take_top()
    hand2.add_card(top)
for t in hand2.cards:
    print(str(t))
discarded_cards = '[' + input('Select cards to discard by giving the index from 0 to {} separated by commas'
                              ' or press \'Enter\' \n'.format(5 - 1)) + ']'
discarded_cards = eval(discarded_cards)
hand2.remove_card(discarded_cards)
player2 = Hand.best_poker_hand(hand2, kinds_of_values)



print(player1 < player2)

# deck, hand = game.start_game()
#game.run_game()
# game.show_game_state(4)

#deck = StandardDeck()
#for c in deck.cards:
#    print(str(c))
#print(','.join([str(c) for c in deck.cards]))


#deck = StandardDeck()
#deck.shuffle()
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

#print("Top card:", end=" ")
#top.print()
#for t in deck.cards:
#    t.print()

#print(len(deck.cards))


#for t in hand.hand:
#    t.print()


index = [2, 0]
#print("Print max index: ", max(index))
#hand.remove_card(index)

#for t in hand.hand:
#    t.print()

'''
#print(hand.hand)
ret = hand.best_poker_hand()
#print(ret)
discarded_cards = (input('Ange vilka kort du vill byta ut. Om du inte vill byta, tryck bara \' enter\' '))
discarded_cards = eval(discarded_cards)
# print(discarded_cards)
hand.remove_card(discarded_cards)
# for t in hand.hand:
#     t.print()

while hand.check_num_of_cards() < max_num_of_cards:
    top = deck.take_top()
    hand.add_card(top)

for t in hand.hand:   khv
    t.print()

ret = hand.best_poker_hand()
'''

