from main import *



#kinds_of_values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
#game = Chicago()
#deck = StandardDeck()
#deck.shuffle()
#num_of_cards = 2

#hand1 = Hand()
#hand2 = Hand()
#dealer = Hand()

# Ge spelare 1 ett kort sen spelare två, tills båda har 2 kort:

#top = deck.take_top()
#hand1.add_card(top)
#top = deck.take_top()
#hand2.add_card(top)
#top = deck.take_top()
#hand1.add_card(top)
#top = deck.take_top()
#hand2.add_card(top)

#print('This is player one\'s hand:')
#for t in hand1.cards:
#    print(str(t))

#print('This is player two\'s hand:')
#for t in hand2.cards:
#    print(str(t))

#player1 = hand1.best_poker_hand(kinds_of_values, [])
#player2 = hand2.best_poker_hand(kinds_of_values, [])

#print('Is player one\'s hand worse than players two\'s?')
#print(player1 < player2)

# Flop:en, alltså dealern tar bort översta kortet och lägger ut 3 kort:

#top = deck.take_top()
#dealer.add_card(top)
#dealer.remove_card([-1])
#top = deck.take_top()
#dealer.add_card(top)
#top = deck.take_top()
#dealer.add_card(top)
#top = deck.take_top()
#dealer.add_card(top)

#for t in dealer.cards:
#    print(str(t))

#num_of_cards = 5
#total_cards1 = hand1.best_poker_hand_total(dealer.cards)
#total_cards2 = hand2.best_poker_hand_total(dealer.cards)

#player1 = hand1.best_poker_hand(kinds_of_values, dealer.cards)
#player2 = hand2.best_poker_hand(kinds_of_values, dealer.cards)


#print(player1 < player2)

# Turn, alltså släng ett kort och lägg ut 4:e kortet:
#num_of_cards = 6
#top = deck.take_top()
#dealer.add_card(top)
#dealer.remove_card([-1])
#top = deck.take_top()
#dealer.add_card(top)

#for t in dealer.cards:
#    print(str(t))

#player1 = hand1.best_poker_hand(kinds_of_values, dealer.cards)
#player2 = hand2.best_poker_hand(kinds_of_values, dealer.cards)

#print(player1 < player2)


# River, alltså släng ett kort och lägg ut 5:e kortet:

num_of_cards = 7
#top = deck.take_top()
#dealer.add_card(top)
#dealer.remove_card([-1])
#top = deck.take_top()
#dealer.add_card(top)

#for t in dealer.cards:
#    print(str(t))

#player1 = hand1.best_poker_hand(kinds_of_values, dealer.cards)
#player2 = hand2.best_poker_hand(kinds_of_values, dealer.cards)

#print(player1 < player2)

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