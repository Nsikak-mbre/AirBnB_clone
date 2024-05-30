#!/usr/bin/python3
"""
    A simple implemented interface, which also serves a
    text based User Interface
"""
import sys
from cmd import Cmd
from models.base_model import BaseModel


class HBNBCommand(Cmd):
    """
        Temporary text based user-interface.
        
        Attributes:
            intro(str): custom welcome message
            prompt(str): The command prompt
    """

    intro = 'Welcome to my shell. Type help or ? to list commands.\n'
    prompt = "(hbnb) "
    __classes = {"BaseModel", "User", "Place", "State", "City", "Amenity", "Review"}

    def do_quit(self, line):
        """Quit command to exit the program"""
        print("** Adios! **")
        return True

    def do_EOF(self, line):
        """EOF also serves to exit program."""
        print("** Bye! **")
        return True

    def emptyline(self):
        """
            Overrides built in behavior, stops Enter button from
            excuting last used command.
        """
        pass
    
    def do_create(self, line):
        """
        Creates new instances of a class & prints the id
        
        Attributes:
            line (str): whatever follows the given command
        """
        class_name = line.split()[0]
        
        if class_name not in self.model:
            print(f"** class '{class_name}' does not exist **")
            return
        
        try:
            attributes = {}
            for item in line.split()[1:]:
                key, value = item.split("=")
                value = eval(value.strip('"'))
                attributes[key] = value
                new_obj = eval(class_name)(**attributes)
                new_obj.save()
                print("{} created: {}".format(class_name, new_obj.id))
        except Exception as e:
            print("** {} **".format(e))
    
    # def do_show(self, line):
        
                
                


if __name__ == '__main__':
    HBNBCommand().cmdloop()
