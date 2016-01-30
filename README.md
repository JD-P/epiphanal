# How To Install #

Right now the program uses no external dependencies, but it does require python 3.x,
it's only been tested with python 3.4 so no promises about working on earlier
versions. Clone the program into a directory of your choosing and run it.

# How To Use #

When started the program will give you a command prompt. The short process for
creating a new reminder deck is to:

Create a new list with the name of your choosing:

new test - Create a new reminder deck with the name 'test'.

Add a couple of reminders:

add Test | 1 - Create a new reminder test with a weight of one. See explanation of
               weight below.

add Test2 | 1 - Same as above but with different name.

Pluck one from the deck to test:

show 1 - Draw a reminder from the list by weight. If you draw multiple reminders
         from the deck there will be no repeats. Therefore you can only draw as
	 many items as exist in the deck.

Save your deck to disk:

save - Save the deck to a file in the .epiphanal folder in your home directory.

Then exit the program:

exit - Leave epiphanal.

When you want to see the reminders later you start up the program and load the
deck:

load test - Load a preexisting deck with a given name.

And use show to draw a reminder from it:

show 1 - See previously.

Then exit again:

exit

# Weight #

Epiphanal draws reminders from an underlying probability distribution in which
each object in the deck is *weighted*. In particular each object takes up a certain
number of 'spots' in the distribution. eg. If you have a deck with two reminders
and one has a weight of 100 and the other has a weight of 1 then the probability
of getting the first object is 100/101 and the probability of getting the second
is 1/101.