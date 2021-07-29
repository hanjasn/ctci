"""
Deck of Cards

Design the data structures for a generic deck of cards. Explain how you would subclass the data structures to implement blackjack.
"""
from enum import Enum
import random


# Standard 52-card deck
class Suit(Enum):
  SPADES = "spades"
  CLUBS = "clubs"
  HEARTS = "hearts"
  DIAMONDS = "diamonds"


class Card:
  def __init__(self, value: int, suit: Suit) -> None:
    self.value = value
    self.suit = suit
  
  def get_value(self) -> int:
    return self.value
  
  def get_suit(self) -> Suit:
    return self.suit
  
  def __str__(self) -> str:
    value = "ace" if self.value == 1 else "jack" if self.value == 11 else "queen" if self.value == 12 else "king" if self.value == 13 else self.value
    return f'{value} of {self.suit.value}'


class Deck:
  def __init__(self, deck: list=None) -> None:
    if deck == None:
      # create default deck with list of Card objects
      deck = []
      for i in range(52):
        value = (i % 13) + 1
        suit = Suit.SPADES if (i // 13) == 0 else Suit.CLUBS if (i // 13) == 1 else\
               Suit.DIAMONDS if (i // 13) == 2 else Suit.HEARTS
        deck.append(Card(value, suit))
    self.cards = deck
    self.dealt_index = 0
  
  # All cards must be back in the deck
  def shuffle(self) -> None:
    random.shuffle(self.cards)
    self.dealt_index = 0
  
  def cards_remaining(self) -> int:
    return len(self.cards) - self.dealt_index
  
  def deal_card(self) -> Card:
    if self.cards_remaining() == 0:
      return None
    
    card = self.cards[self.dealt_index]
    self.dealt_index += 1
    return card
  
  def deal_cards(self, num: int) -> list:
    if num > self.cards_remaining():
      return None
    
    cards = []
    for i in range(num):
      cards.append(self.cards[self.dealt_index + i])
    self.dealt_index += num
    return cards
  
  def __str__(self) -> str:
    result = ""
    for c in self.cards:
      result += str(c) + "\n"
    return result