# ____ ra.. ______ sh..
# # Each instance of Card  should have a suit ("Hearts", "Diamonds", "Clubs", or "Spades").
# # Each instance of Card  should have a value ("A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K").
# # Card 's __repr__  method should display the card's value and suit (e.g. "A of Clubs", "J of Diamonds", etc.)
#
#
# c_ Card
#     ___ - ____ value suit
#         ____.?  ?
#         ____.?  ?
#
#     ___ -r
#         # r_ "{} of {}".format(____.value, ____.suit)
#         r_ _* ____.v..| of ____.s..|
#
# # Each instance of Deck  should have a cards attribute with all 52 possible instances of Card .
# # Deck  should have an instance method called count  which returns a count of how many cards remain in the deck.
# # Deck 's __repr__  method should display information on how many cards are in the deck (e.g. "Deck of 52 cards",
# # "Deck of 12 cards", etc.)
# # Deck  should have an instance method called _deal  which accepts a number and removes at most that many cards
# # from the deck (it may need to remove fewer if you request more cards than are currently in the deck!).
# # If there are no cards left, this method should r_ a ValueError  with the message "All cards have been dealt".
# # Deck  should have an instance method called shuffle  which will shuffle a full deck of cards.
# # If there are cards missing from the deck, this method should r_ a ValueError  with the message
# # "Only full decks can be shuffled".
# # Deck  should have an instance method called deal_card  which uses the _deal  method to deal a single card
# # from the deck.
# # Deck  should have an instance method called deal_hand  which accepts a number and uses the _
# # deal  method to deal a list of cards from the deck.
#
#
# c_ Deck
#     ___ -
#         suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
#         values = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']
#         ____.cards _ C.. value suit ___ s.. __ s.. ___ v.. __ v..
#
#     ___ -r
#         r_ _*Deck of |____.co..| cards"
#
#     ___ count ____
#         r_ le. ____.c..
#
#     ___ _deal ____ num
#         count = ____.c..
#         actual = mi. co..,n..
#         __ c.. __ 0
#             r... V.. "All cards have been dealt"
#         cards = ____.c.. |-a..;
#         ____.c.. = ____.c.. ;-a..
#         r_ c..
#
#     ___ deal_card ____
#         r_ ____._d.. 1 0
#
#     ___ deal_hand ____ hand_size
#         r_ ____._d.. ?
#
#     ___ shuffle ____
#         __ ____.co.. < 52
#             r.. V... "Only full decks can be shuffled"
#
#         sh.. ____.c..
#         r_ ____
#
#
# d = ?
# ?.s..
# card = ?.d_c..
# print ?
# hand = ?.d_h.. 50
# card2 = ?.d_c..
# print ?
# print ?.c..
# card2 = ?.d_c..
#
# # print(d.cards)
