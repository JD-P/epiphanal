# Introduction #

Most to-do lists, project-lists and the like are *sequential*. You're expected to
read them linearly every time. Of course, we don't do this. We scan them, we skim,
and every other technique humans use to kinda read something when their eyes glaze
over. The longer a to-do list or project list gets, the more likely we are to just
give up on it entirely. The basic problem is that our attention and patience are
finite and we let these lists grow so large that it's unreasonable to expect
ourselves to actually read them wholesale.

Enter expected value. For something like a project list especially, we can imagine
an *expected value* of reading the list for a given number of items. On a fifty
item list one in every five ideas might be good enough to be worth reading again.
The problem with trying to read the list at random is that you have to ignore all
the other items on the list as visual noise. Epiphanal solves this problem by
letting you define a probability distribution over all the items in the list
and then grabbing a subsection from this distribution to read.

# How To Install #

Right now the program uses no external dependencies, but it does require python 3.x,
it's only been tested with python 3.4 so no promises about working on earlier
versions. Clone the program into a directory of your choosing and run it.

# How To Use #

When started the program will give you a command prompt. The short process for
creating a new reminder deck is to:

Create a new list with the name of your choosing:

    <epiphanal> new test - Create a new reminder deck with the name 'test'.

Add a couple of reminders:

    <epiphanal> add Test | 1 - Create a new reminder test with a weight of one. See explanation of
                               weight below.

    <epiphanal> add Test2 | 1 - Same as above but with different name.

Pluck one from the deck to test:

    <epiphanal> show 1 - Draw a reminder from the list by weight. If you draw multiple reminders
                from the deck there will be no repeats. Therefore you can only draw as
	        many items as exist in the deck.

Or use 'show all' to see everything:

    <epiphanal> show all - Show every item in the reminder deck.

Save your deck to disk:

    <epiphanal> save - Save the deck to a file in the .epiphanal folder in your home directory.

Then exit the program:

    <epiphanal> exit - Leave epiphanal.

When you want to see the reminders later you start up the program and load the
deck:

    <epiphanal> load test - Load a preexisting deck with a given name.

And use show to draw a reminder from it:

    <epiphanal> show 1 - See previously.

Then exit again:

    <epiphanal> exit

It's important to keep in mind that any changes to the deck will have to be saved
with the 'save' command:

    <epiphanal> add Test3 | 1

    <epiphanal> save

# Weight #

Epiphanal draws reminders from an underlying probability distribution in which
each object in the deck is *weighted*. In particular each object takes up a certain
number of 'spots' in the distribution. eg. If you have a deck with two reminders
and one has a weight of 100 and the other has a weight of 1 then the probability
of getting the first object is 100/101 and the probability of getting the second
is 1/101.