# epiphanal - A program for remembering things probabilistically

import json
import random

class ReminderDeck:
    """The deck which the program saves reminders to and draws from to display
    reminders to the user.

    The deck proper's data structure is a list sorted in nonincreasing order of 
    strings representing the reminders and weights for how often the reminders
    should occur, and then a second list which is created by adding the first 
    weight of the first list, and then adding every proceeding weight to the
    sum of the weights preceeding it. For example, imagine we have the following 
    table of reminders and weights:

    A 3000
    B 1500
    C 1000
    D 500
    E 250
    F 125

    Then the second list would look like:

    3000, 4500, 5500, 6000, 6250, 6375

    To draw a card from the deck, we choose a random number between 6375 and 0.
    We then do a binary search on the second list to determine how far into the
    list our draw is. In particular, from a given place in the second list our
    draw is at the same position. Let's say we draw 3300. That puts us past the
    first value, 3000, but it puts us below the second value, 4500. B has 1500
    places in our 6375 long line of numbers we draw from. Hence its range would
    terminate at 4500, if we're above 3000 but below 4500 our draw in list one
    would be position two. This means that each individual draw from the deck 
    runs in logarithmic time. Insertions and deletions are both O(n), because of
    the need to recalculate the second list after each."""
    def __init__(self, filepath=None):
        if filepath:
            deck_file = open(filepath)
            self._reminders = json.load(deck_file)
        else:
            self._reminders = []
        self._weight_ranges = []
        if self._reminders:
            accumulator = 0
            for reminder in self._reminders:
                accumulator += reminder
                self._weight_ranges.append(accumulator - 1)
                
    def draw(self, quantity):
        """Draw a number of reminders <quantity> from the deck. Each draw is 
        guarunteed to produce a unique object. If you call draw with a quantity
        of ten you will get ten unique reminders from the deck as output.

        Each reminder is of the form:

        (<STRING>, <INTEGER WEIGHT>)

        The entire set is returned as a list sorted in nonincreasing order."""
        if quantity > len(self._reminders):
            raise self.OverDrawError
        distribution = self._weight_ranges[-1] + 1
        previous_ranges = []
        for i in range(quantity):
            picked = False
            while not picked:
                drawn = random.randrange(distribution)
                if previous_ranges:
                    for previous in previous_ranges:
                        if drawn < (previous[0] + 1) or drawn > previous[1]:
                            continue

                        else:
                            break
    def _binary_range_search(self, sequence, position):
        """Search the weight ranges for a given position and return the position 
        in the reminder list that the position falls into."""
        if position > sequence[-1]:
            raise self.OverDrawError
        head = 0
        tail = len(sequence) - 1
        while True:
            if head:
                midpoint = (head + tail) / 2
                if position > sequence[midpoint]:
                    if position > sequence[midpoint + 1]:
                        head = midpoint + 1
                    else:
                        return midpoint + 1
                elif position < sequence[midpoint]:
                    try:
                        if position > sequence[midpoint - 1]:
                            return midpoint
                        else:
                            tail =  midpoint - 1
                    except IndexError:
                        return midpoint
                else:
                    return midpoint
            else:
                midpoint = (head + 1 + tail) / 2
                if position > sequence[midpoint]:
                    if position > sequence[midpoint + 1]:
                        head = midpoint + 1
                    else:
                        return midpoint + 1
                elif position < sequence[midpoint]:
                    try:
                        if position > sequence[midpoint - 1]:
                            return midpoint
                        else:
                            tail =  midpoint - 1
                    except IndexError:
                        return midpoint
                else:
                    return midpoint
                        
    class OverDrawError:
        """Error raised when more items are requested from a method which pulls
        from a probability distribution than the distribution can provide."""
        pass
