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
    hand1 = Hand()
    hand2 = Hand()
    card1 = JackCard(Suits.clubs)
    card2 = 1
    hand1.add_card(card1)
    with assert_raises(TypeError):
        hand2.add_card(card2)

def test_lesser_than():
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
