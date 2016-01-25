# epiphanal - A program for remembering things probabilistically

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
    the need to recalculate the second list after each.
    
