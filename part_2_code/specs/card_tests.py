import unittest

from src.card import Card
from src.card_game import CardGame

class TestCard(unittest.TestCase):

    def setUp(self):
        self.card1 = Card('Clubs', 1)
        self.card2 = Card('Diamonds', 4)
        self.card3 = Card('Spades', 5)
        self.card4 = Card('Hearts', 7)

    def test_card__suit(self):
        self.assertEqual('Clubs', self.card1.suit)  
        self.assertEqual('Diamonds', self.card2.suit)
        self.assertEqual('Spades', self.card3.suit)
        self.assertEqual('Hearts', self.card4.suit) 

    def test_card__value(self):
        self.assertEqual(1, self.card1.value)  
        self.assertEqual(4, self.card2.value)
        self.assertEqual(5, self.card3.value)
        self.assertEqual(7, self.card4.value) 