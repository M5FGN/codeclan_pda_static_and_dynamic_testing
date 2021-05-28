import unittest

from src.card import Card
from src.card_game import CardGame

class TestCardGame(unittest.TestCase):

    def setUp(self):
        self.card1 = Card('Clubs', 1)
        self.card2 = Card('Diamonds', 4)
        self.card3 = Card('Spades', 5)
        self.card4 = Card('Hearts', 7)

        self.card_game = CardGame()


    def test_check_for_ace(self):
        self.assertEqual(True, self.card_game.check_for_ace(self.card1))
        self.assertEqual(False, self.card_game.check_for_ace(self.card2))

    def test_highest_card(self):
        self.assertEqual(self.card4, self.card_game.highest_card(self.card2, self.card4))
        self.assertEqual(self.card2, self.card_game.highest_card(self.card1, self.card2))
    
    def test_cards_total(self):
        cards = [self.card1, self.card2, self.card3, self.card4]
        cardTotal = self.card_game.cards_total(cards)
        self.assertEqual("You have a total of 17", cardTotal)