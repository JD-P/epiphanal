from epiphanal import *
import unittest
import cProfile
import random
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--speed", action='store_true')
arguments = parser.parse_args()

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
        deck.remove(0)
        self.assertFalse(deck.all())

    def test_all(self):
        deck = ReminderDeck()
        deck.insert("A", 10)
        deck.insert("B", 10)
        a = deck.all()
        a.sort()
        self.assertTrue(a == [("A", 10), ("B", 10)])

class TestReminderDeckSpeed(unittest.TestCase):
    def test_speed(self):
        deck = ReminderDeck()
        for i in range(10000):
            chars = (chr(random.randrange(128)) + chr(random.randrange(128)) +
                     chr(random.randrange(128)) + chr(random.randrange(128)))
            deck.insert(chars, random.randrange(10000))
        cProfile.runctx('deck.draw(100)', globals(), locals())
                
if __name__ == '__main__':
    unittest.main()
