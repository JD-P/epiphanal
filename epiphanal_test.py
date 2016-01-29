from epiphanal import *
import unittest

class TestReminderDeck(unittest.TestCase):
    def test_draw(self):
        # Test that draw returns the right number of items
        deck = ReminderDeck()
        deck.insert("A", 10)
        deck.insert("B", 10)
        deck.insert("C", 10)
        deck.insert("D", 10)
        self.assertTrue(len(deck.draw(3)) == 3)

        # Test that items returned by draw are unique
        self.assertTrue(len(set(deck.draw(3))) == 3)

    def test_insert(self):
        deck = ReminderDeck()
        deck.insert("A", 10)
        self.assertTrue(deck.draw(1) == [("A", 10)])

    def test_remove(self):
        deck = ReminderDeck()
        deck.insert("A", 10)
        deck.remove("A")
        self.assertFalse(deck.all())

if __name__ == '__main__':
    unittest.main()
