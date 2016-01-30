# epiphanal - A program for remembering things probabilistically

import json
import random

class ReminderDeck:
    """The deck which the program saves reminders to and draws from to display
    reminders to the user.

    The deck proper's data structure is a dictionary. This dictionary is of the 
    form:

    {<REMINDER_STRING>:<REMINDER_WEIGHT>}

    Where a reminder string is a string with the text of the reminder. A reminder
    weight is the number of positions the reminder takes up in the underlying
    probability distribution you draw from."""
    def __init__(self, filepath=None):
        if filepath:
            deck_file = open(filepath)
            self._reminders = json.load(deck_file)
        else:
            self._reminders = {}
                
    def draw(self, quantity):
        """Draw a number of reminders <quantity> from the deck. Each draw is 
        guarunteed to produce a unique object. If you call draw with a quantity
        of ten you will get ten unique reminders from the deck as output.

        Each reminder is of the form:

        (<STRING>, <INTEGER WEIGHT>)

        The entire set is returned as a list sorted in nonincreasing order."""
        if quantity > len(self._reminders):
            raise self.OverDrawError
        weight_distribution = 0
        reminder_list = []
        for reminder in self._reminders:
            weight_distribution += self._reminders[reminder]
            reminder_list.append((reminder, self._reminders[reminder]))
        index_distribution = len(reminder_list)
        output = []
        for i in range(quantity):
            signal = len(output)
            while signal == len(output):
                for weight in reminder_list:
                    index = random.randrange(index_distribution)
                    reminder = reminder_list[index]
                    die = WeightedDie(reminder[1], weight_distribution)
                    roll = die.roll()
                    if roll:
                        outcome = reminder_list.pop(index)
                        output.append(outcome)
                        index_distribution -= 1
                        weight_distribution -= outcome[1]
                        break
                    else:
                        continue
        return output

    def insert(self, reminder_string, reminder_weight):
        """Insert a reminder into the deck.

        reminder_string: The string of text that is the reminder proper.
        reminder_weight: An integer weight that specifies how many spots in 
        the underlying probability distribution the reminder takes up."""
        self._reminders[reminder_string] = reminder_weight
        return True

    def remove(self, reminder_string):
        """Remove a reminder from the deck.

        reminder_string: The unique string comprising the reminder proper which
        is used as the key to remove the reminder."""
        self._reminders.pop(reminder_string)
        return True

    def all(self):
        """Return all the entries in the reminder dictionary."""
        output = []
        for reminder in self._reminders:
            output.append((reminder, self._reminders[reminder]))
        return output
    
    class OverDrawError(Exception):
        """Error raised when more items are requested from a method which pulls
        from a probability distribution than the distribution can provide."""
        pass

class WeightedDie:
    """Represents an individual roll for whether a reminder is picked by a draw 
    or not. The basic algorithm is that reminders are chosen at random and then
    an rng rolls against the 'range' out of the total distribution the reminders
    weight takes up."""
    def __init__(self, weight, distribution):
        self.weight = weight
        self.distribution = distribution

    def roll(self):
        outcome = random.randrange(self.distribution)
        if outcome <= self.weight:
            return True
        else:
            return False
