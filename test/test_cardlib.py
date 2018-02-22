from nose.tools import assert_raises
from main import *


def test_math():
    assert 1 + 1 == 2
    assert 2 * 2 + 3 == 7
# It is important to also test strange inputs,
# like dividing what zero and see that good exceptions are thrown.
# What happens if you try create a card with numerical value 0 or -1?
    with assert_raises(ZeroDivisionError):
        1 / 0


def test_full_house():
    """
    Creates a Hand that contains a known full house and checks that best_poker_hand returns the correct values
    """
    hand3 = Hand()
    for color in Suits:
        hand3.cards.append(JackCard(color))
    hand3.remove_card([-1])
    for color in Suits:
        hand3.cards.append(QueenCard(color))
    hand3.remove_card([-1])
    #hand3.remove_card([-1])
    for t in hand3.cards:
        #print(str(t))
        pass
    player3 = hand3.best_poker_hand(kinds_of_values, [])
    assert player3.hand_rank == PokerHandType.full_house.value
    assert player3.rank_value == ((QueenCard.get_value(None), JackCard.get_value(None)))


def test_hand():
    """
    Creates a Hand object and attempts to add a PlayingCard and something that is not a PlayingCard, in this case
    an int with expected error TypeError
    """
    hand1 = Hand()
    hand2 = Hand()
    card1 = JackCard(Suits.clubs)
    card2 = 1
    hand1.add_card(card1)
    with assert_raises(TypeError):
        hand2.add_card(card2)


def test_lesser_than():
    """
    Creates a total of two hands with known cards and which hand is the best. Checks that the lesser than and
    best_poker_hand methods work as they should.
    """
    hand1 = Hand()
    for color in Suits:
        hand1.cards.append(JackCard(color))
    hand1.remove_card([-1])
    hand1.remove_card([-1])
    for color in Suits:
        hand1.cards.append(QueenCard(color))
    hand1.remove_card([-1])
    hand1.remove_card([-1])

    hand2 = Hand()
    for color in Suits:
        hand2.add_card(AceCard(color))
    hand2.remove_card([-1])

    best_hand_1 = hand1.best_poker_hand(kinds_of_values, [])
    best_hand_2 = hand2.best_poker_hand(kinds_of_values, [])
    assert best_hand_1 < best_hand_2


def test_remove_card():
    """
    Creates a hand with four cards and tries to remove the card with index 5. IndexError is expected.
    """
    hand = Hand()
    for color in Suits:
        hand.add_card(NumberedCard(color, color))
    with assert_raises(IndexError):
        hand.remove_card([5])


def test_deck():
    """
    Creates a StandardDeck and checks its methods and properties
    """
    deck = StandardDeck()
    top_card_1 = deck.cards[0]
    assert len(deck.cards) == 52    # Check number of cards
    assert len(set(deck.cards)) == 52   # Check number of individual elements
    deck.shuffle()
    assert top_card_1 != deck.cards[0]  # Check that if shuffles
    assert len(set(deck.cards)) == 52   # Check number of individual cards after shuffle
    top_card_2 = deck.cards[0]
    top_card_3 = deck.take_top()
    assert top_card_2 == top_card_3 and len(deck.cards) == 51   # Check that take_top takes the top card and removes it
    assert top_card_3 not in deck.cards


def test_straight_flush():
    hand = Hand()
    for i in range(5):
        hand.add_card(NumberedCard(i+2, Suits.clubs))
    best_hand = hand.best_poker_hand(kinds_of_values, [])
    assert best_hand.rank_value == i+2 and best_hand.hand_rank.value == PokerHandType.straight_flush


def test_compare_pokerhands():
    pass


