from epiphanal import *
import os
import cmd

class EpiphanalLineInterface(cmd.Cmd):
    intro = "Epiphanal 0.1. Type help or ? for a command listing."
    prompt = "<epiphanal> "

    def do_load(self, arg):
        """Load in a ReminderDeck. Takes a single argument which is the name of
        the deck. Decks can only have alphanumeric characters and the underscore/
        dash characters.

        Examples:

        load projects

        load my_list

        load my-list"""
        if not arg:
            print("Load requires a deck name as an argument. See 'help load' for"
                  " more details.")
            return False
        filename = arg + ".json"
        home = os.path.expanduser("~")
        filepath = os.path.join(home, ".epiphanal", filename)
        try:
            self.deck = ReminderDeck(filepath)
        except FileNotFoundError:
            print("Couldn't find the deck at: " + "'" + filepath + "' " +
                  "See 'help new' to create one.")
            
    def do_save(self, unused_arg):
        """Save the reminder deck to disk. Takes no arguments."""
        try:
            self.deck.save()
        except AttributeError:
            print("No reminder deck loaded. See 'help load' or 'help new' to load",
                  "an existing deck or create a new one.")

    def do_list(self, arg):
        """List the reminder decks that are stored in the system. Takes no 
        arguments.

        Example: list"""
        for deck in os.listdir(os.path.join(os.path.expanduser("~"), ".epiphanal")):
            print(deck[:-5])
            
    def do_new(self, arg):
        """Create a new reminder deck with the name given by argument.

        Example:

        new projects - Create a reminder deck with the name 'projects'."""
        if not arg:
            print("New requires a deck name as an argument. See 'help new' for "
                  "more details.")
            return False
        alphanumeric_dash_underscore = ("abcdefghijklmnopqrstuvwxyz"
                                        "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
                                        "-_")
        for character in arg:
            if character not in alphanumeric_dash_underscore:
                print("Character: " + "'" + character + "'" + " is not alphanumeric.")
                return False
        filename = arg + ".json"
        home = os.path.expanduser("~")
        filepath = os.path.join(home, ".epiphanal", filename)
        try:
            new_file = open(filepath, "w")
        except FileNotFoundError:
            os.makedirs(os.path.split(filepath)[0])
            new_file = open(filepath, "w")
        json.dump([], new_file)
        new_file.close()
        self.deck = ReminderDeck(filepath)
        
        
    def do_show(self, arg):
        """Show n reminders from the reminder deck or all of them, depending on 
        argument.

        Examples:

        show all - Shows all the items in the reminder deck.

        show 10 - Draws ten unique items from the deck by weight and displays them.
        
        Asking for more items than exist in the deck returns all items."""
        if arg == 'all':
            try:
                items = self.deck.all()
            except AttributeError:
                print("No reminder deck loaded. See 'help load' or 'help new' to load",
                      "an existing deck or create a new one.")
                return False
        else:
            try:
                try:
                    items = self.deck.draw(int(arg))
                except AttributeError:
                    print("No reminder deck loaded. See 'help load' or 'help new' to load",
                          "an existing deck or create a new one.")
                    return False
                except ValueError:
                    print("The argument to show should be an integer quantity of"
                          " reminders to pull from the deck. See 'help show' for"
                          " more details.")
                    return False
            except ReminderDeck.OverDrawError:
                try:
                    items = self.deck.all()
                except AttributeError:
                    print("No reminder deck loaded. See 'help load' or 'help new' to load",
                          "an existing deck or create a new one.")
                    return False
        for item in enumerate(items):
            print(item[0], item[1][0], item[1][1], sep=" | ")
        
    def do_add(self, args):
        """Add a reminder to the reminder deck. Arguments are seperated by the 
        vertical bar | and as follows:

        reminder_string | weight

        As an example:

        Project: Probabilistic to-do list and project list | 10"""
        arguments = args.split('|')
        try:
            self.deck.insert(arguments[0].strip(), int(arguments[1].strip()))
        except AttributeError:
            print("No reminder deck loaded. See 'help load' or 'help new' to load",
                  "an existing deck or create a new one.")
        except IndexError:
            print("Improper command. Valid commands are a reminder string seperated",
                  "by an integer weight. See 'help add' for more details.")
            
    def do_remove(self, arg):
        """Remove an item from the reminder deck by its index.

        Examples:

        remove 0 - Remove the first element in the reminder deck.

        remove 1 - Remove the second element in the reminder deck.

        These are not typos, the reminder deck is zero-indexed, meaning it starts
        counting its contents at zero rather than one. It's also important to note
        that when an item is removed the index of all other items is decremented by
        one. So if you have two reminders and you remove the first, you would remove
        the second with the same command."""
        try:
            self.deck.remove(int(arg))
        except AttributeError:
            print("No reminder deck loaded. See 'help load' or 'help new' to load",
                  "an existing deck or create a new one.")
            
    def do_exit(self, unused_arg):
        return True

interface = EpiphanalLineInterface()
interface.cmdloop()
