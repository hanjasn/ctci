import unittest
from solution import *


class DeskTest(unittest.TestCase):
  def test_1(self) -> None:
    deck = Deck()
    print(deck)
    deck.shuffle()
    print(deck)
  
  def test_2(self) -> None:
    deck = Deck()
    self.assertEqual(52, deck.cards_remaining())
  
  def test_3(self) -> None:
    deck = Deck()
    cards = Deck(deck.deal_cards(3))
    self.assertEqual("ace of spades\n2 of spades\n3 of spades\n", str(cards))
    self.assertEqual(49, deck.cards_remaining())
  
  def test_4(self) -> None:
    deck = Deck()
    for i in range(10): deck.deal_card()
    card = deck.deal_card()
    self.assertEqual("jack of spades", str(card))