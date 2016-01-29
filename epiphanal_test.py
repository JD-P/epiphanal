from epiphanal import *
import unittest

class TestReminderDeck(unittest.TestCase):
    def test_draw(self):
        deck = ReminderDeck()
        deck.insert("A", 10)
        deck.insert("B", 10)
        deck.insert("C", 10)
        deck.insert("D", 10)
        self.assertTrue(len(deck.draw(3)) == 3)

if __name__ == '__main__':
    unittest.main()
