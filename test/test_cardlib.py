from nose.tools import assert_raises
from main import *


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

    player3 = hand3.best_poker_hand([])
    assert player3.hand_rank == PokerHandType.full_house.value
    assert player3.rank_value == (QueenCard.get_value(None), JackCard.get_value(None))


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

    best_hand_1 = hand1.best_poker_hand([])
    best_hand_2 = hand2.best_poker_hand([])
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
    assert len(deck.cards) == 52    # Check number of cards
    cards = [(card.get_value(), card.get_suit().value) for card in deck.cards]
    assert len(set(cards)) == 52   # Check number of individual elements
    deck_standard = StandardDeck()
    deck.shuffle()
    card_list_1 = []
    card_list_2 = []
    for i, card in enumerate(deck.cards):
        card_list_1.append(card.get_value())
        card_list_2.append(deck_standard.cards[i].get_value())
    assert card_list_1 != card_list_2   # Check that if shuffles
    cards = [(card.get_value(), card.get_suit().value) for card in deck.cards]
    assert len(set(cards)) == 52   # Check number of individual cards after shuffle
    top_card_2 = deck.cards[0]
    top_card_3 = deck.take_top()
    assert top_card_2 == top_card_3 and len(deck.cards) == 51   # Check that take_top takes the top card and removes it
    assert top_card_3 not in deck.cards


def test_straight_flush():
    """
    Creates a Hand with cards representing a straight flush. This test method tests if best_poker_hand returns
    the correct PokerHand for this hand
    """
    hand1 = Hand()
    hand2 = Hand()
    for i in range(5):
        hand1.add_card(NumberedCard(i+2, Suits.clubs))
        hand2.add_card(NumberedCard(i+2, Suits.clubs))
    hand2.add_card(QueenCard(Suits.spades))
    best_hand1 = hand1.best_poker_hand([])
    best_hand2 = hand2.best_poker_hand([])

    assert best_hand1.rank_value == (i+2, i+2) and best_hand1.hand_rank == PokerHandType.straight_flush.value
    assert best_hand2.rank_value == (i+2, hand2.cards[-1].get_value()) and best_hand2.hand_rank == PokerHandType.straight_flush.value

    assert best_hand1 < best_hand2


def test_compare_pokerhands():
    """
    This method creates two known Hands where it is known which hand is the greater. The method test the lesser than
    command for PokerHands
    """
    hand1 = Hand()
    hand2 = Hand()
    for i in range(5):
        hand1.add_card(NumberedCard(i+2, Suits.spades))
        hand2.add_card(NumberedCard(i+2, Suits.spades))
    best_hand1 = hand1.best_poker_hand([])
    best_hand2 = hand2.best_poker_hand([])
    assert not (best_hand1 < best_hand2)
    hand2.add_card(NumberedCard(i+3, Suits.spades))
    best_hand3 = hand2.best_poker_hand([])
    assert best_hand1 < best_hand3

def test_sort_hand():
    # Create a hand that is manually sorted mainly by suit, secondary by value
    man_sorted = Hand()
    man_sorted.add_card(NumberedCard(2, Suits.clubs))
    man_sorted.add_card(QueenCard(Suits.clubs))
    man_sorted.add_card(NumberedCard(10, Suits.diamonds))
    man_sorted.add_card(KingCard(Suits.diamonds))
    man_sorted.add_card(NumberedCard(7, Suits.spades))
    man_sorted.add_card(AceCard(Suits.spades))
    man_sorted.add_card(NumberedCard(4, Suits.hearts))

    # Create a manually shuffled hand by the same cards as in man_sorted
    man_shuffled = Hand()
    man_shuffled.add_card(NumberedCard(2, Suits.clubs))
    man_shuffled.add_card(NumberedCard(4, Suits.hearts))
    man_shuffled.add_card(NumberedCard(10, Suits.diamonds))
    man_shuffled.add_card(QueenCard(Suits.clubs))
    man_shuffled.add_card(AceCard(Suits.spades))
    man_shuffled.add_card(KingCard(Suits.diamonds))
    man_shuffled.add_card(NumberedCard(7, Suits.spades))

    # Sort the hand with sort_hand method for Hand() (comment this line to assert Error)
    man_shuffled.sort_hand()

    # Determine the order of suits and values in the manually sorted hand
    man_sorted_card_values = []
    man_sorted_card_suits = []
    for card in man_sorted.cards:
        man_sorted_card_values.append(card.get_value())
        man_sorted_card_suits.append(card.get_suit())

    # Determine the order of suits and values in the shuffled and then sorted hand
    man_shuffled_card_values = []
    man_shuffled_sorted_card_suits = []
    for card in man_shuffled.cards:
        man_shuffled_card_values.append(card.get_value())
        man_shuffled_sorted_card_suits.append(card.get_suit())

    # The number of cards should be the same
    assert len(man_sorted.cards) == len(man_shuffled.cards)
    # The suits should be in the same order
    assert man_sorted_card_suits == man_shuffled_sorted_card_suits
    # The values should be in the same order
    assert man_sorted_card_values == man_shuffled_card_values


def test_one_pair():
    # Create a Hand() with one pair and some random other cards
    pair_hand = Hand()
    value = 5
    pair_hand.add_card(NumberedCard(value, Suits.diamonds))
    pair_hand.add_card(NumberedCard(value, Suits.clubs))
    pair_hand.add_card(AceCard(Suits.diamonds))
    pair_hand.add_card(KingCard(Suits.clubs))
    pair_hand.add_card(JackCard(Suits.clubs))
    pair_hand.add_card((NumberedCard(6, Suits.spades)))
    # pair_hand.add_card(AceCard(Suits.clubs)) (Uncomment this to verify that two pairs assert Error)

    best_hand = pair_hand.best_poker_hand([])
    pair_hand_rank_value = (value, (AceCard.get_value(None), KingCard.get_value(None), JackCard.get_value(None)))

    # Determine if the hand_rank has the right value (1)
    assert best_hand.hand_rank == PokerHandType.pair.value
    # Determine if the three cards with the highest value other than the pair is saved as rank_value
    assert best_hand.rank_value == pair_hand_rank_value


def test_three_of_a_kind():
    """
    This method creates two hands, both with three of a kind and compares them to test that the return from
    best_poker_hand is correct. It also tests the lesser than command for three of a kind.
    """
    hand1 = Hand()
    hand2 = Hand()
    for colour in Suits:
        hand1.add_card(JackCard(colour))
        hand2.add_card(QueenCard(colour))
    hand1.remove_card([-1])
    hand2.remove_card([-1])
    best_hand1 = hand1.best_poker_hand([])
    best_hand2 = hand2.best_poker_hand([])
    hand_rank = PokerHandType.three_of_a_kind
    assert best_hand1.hand_rank == hand_rank and best_hand2.hand_rank == hand_rank
    assert best_hand1.rank_value == ((11, 11, 11)) and best_hand2.rank_value == ((12, 12, 12))
    assert best_hand1 < best_hand2


def test_four_of_a_kind():
    """
    This method creates two hands, both with four of a kind and compares them to test that the return from
    best_poker_hand is correct. It also tests the lesser than command for four of a kind.
    """
    hand1 = Hand()
    hand2 = Hand()
    for colour in Suits:
        hand1.add_card(QueenCard(colour))
        hand2.add_card(JackCard(colour))
    best_hand1 = hand1.best_poker_hand([])
    best_hand2 = hand2.best_poker_hand([])
    assert best_hand1.hand_rank == best_hand2.hand_rank == PokerHandType.four_of_a_kind.value
    assert best_hand2 < best_hand1


def test_two_pair():
    """
    This method creates two hands, both with two pair and compares them to test that the return from
    best_poker_hand is correct. It also tests the lesser than command for two pair.
    """
    hand1 = Hand()
    hand2 = Hand()
    hand1.add_card(NumberedCard(3, Suits.spades))
    hand1.add_card(NumberedCard(3, Suits.hearts))
    hand1.add_card(NumberedCard(4, Suits.spades))
    hand1.add_card(NumberedCard(4, Suits.hearts))

    hand2.add_card(NumberedCard(3, Suits.clubs))
    hand2.add_card(NumberedCard(3, Suits.diamonds))
    hand2.add_card(NumberedCard(2, Suits.clubs))
    hand2.add_card(NumberedCard(2, Suits.diamonds))

    best_hand1 = hand1.best_poker_hand([])
    best_hand2 = hand2.best_poker_hand([])

    assert best_hand1.hand_rank == best_hand2.hand_rank == PokerHandType.two_pair.value
    assert best_hand1.rank_value == (4, 3, 4) and best_hand2.rank_value == (3, 2, 3)
    assert best_hand2 < best_hand1
    assert not best_hand1 < best_hand2


def test_high_card():
    """
    This method creates two hands, where the best_poker_hand should return high_card only. It also test if the lesser
    than works for high_card as well.
    """
    hand1 = Hand()
    hand2 = Hand()
    hand1.add_card(NumberedCard(5, Suits.diamonds))
    hand1.add_card(NumberedCard(8, Suits.spades))
    hand1.add_card(NumberedCard(10, Suits.hearts))
    hand1.add_card(NumberedCard(2, Suits.diamonds))

    hand2.add_card(NumberedCard(5, Suits.hearts))
    hand2.add_card(JackCard(Suits.clubs))
    hand2.add_card(NumberedCard(3, Suits.diamonds))

    best_hand1 = hand1.best_poker_hand([])
    best_hand2 = hand2.best_poker_hand([])

    assert best_hand1.hand_rank == best_hand2.hand_rank == PokerHandType.high_card.value
    assert best_hand1.rank_value == (10, 8, 5, 2) and best_hand2.rank_value == (11, 5, 3)
    assert best_hand1 < best_hand2



