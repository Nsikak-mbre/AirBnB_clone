#!/usr/bin/python3
"""
    A simple implemented interface, which also serves a
    text based User Interface
"""

from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models import storage
import models


class HBNBCommand(Cmd):
    """
        Temporary text based user-interface.

        Attributes:
            intro(str): custom welcome message
            prompt(str): The command prompt
    """

    intro = 'Welcome to my shell. Type help or ? to list commands.\n'
    prompt = "(hbnb) "
    __classes = {
            "BaseModel",
            "User",
            "Place",
            "State",
            "City",
            "Amenity",
            "Review"
            }

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

    def do_create(self, arg):
        """
        Creates new instances of a class & prints the id

        Attributes:
            arg (str): whatever follows the given command
        """
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        if args[0] not in globals():
            print("** class doesn't exist **")
            return
        cls = globals()[args[0]]
        new_instance = cls()
        new_instance.save
        print(new_instance.id)

    def do_show(self, arg):
        """
        Prints the string representation of an,
        instance based on class name and id

        Attributes:
            arg (str): the insatnce to be printed.

        """
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        if args[0] not in globals():
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = f"{args[0]}.{args[1]}"
        instance = models.storage.all().get(key)
        if instance:
            print(instance)
        else:
            print("** no instance found **")

    def do_destroy(self, arg):
        """
        Deletes an instance based on class name and id.

        Attributes:
            arg (str): the instance to be destroyed.
        """
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        if args[0] not in globals():
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = f"{args[0]}.{args[1]}"
        if key in models.storage.all():
            del models.storage.all()[key]
            models.storage.save()
        else:
            print("** no instance found **")

    def do_all(self, arg):
        """
        Prints all string representation,
        of all instances based or not on the class name.

        Attributes:
            arg (str): all the class instancess will be printed out.
        """
        instance = []
        if arg:
            if arg not in globals():
                print("** class doesn't exist **")
                return
            for key, obj in models.storage.all().items():
                if key.startswith(arg):
                    instance.append(str(obj))
        else:
            for obj in models.storage.all().values():
                instance.append(str(obj))
        print(instance)

    def do_update(self, arg):
        """
        Updates an instance based on the class name,
        and id by adding or updating attribute.

        Attributes:
            arg (str): the unsatnce to be updated.
        """
        args = arg.split()
        if not args:
            print("** class name missing **")
            return
        if args[0] not in globals():
            print("** class doesn't exist **")
            return
        key = f"{args[0]}.{args[1]}"
        if key not in models.storage.all():
            print("** no instance found **")
            return
        if len(args) < 3:
            print("** attribute name missing **")
            return
        if len(args) < 4:
            print("** value missing **")
            return
        instance = models.storage.all()[key]
        attr_name = args[2]
        attr_value = args[3].strip('"')
        if attr_name in ('id', 'created_at', 'updated_at'):
            return
        try:
            attr_value = eval(attr_value)
        except (NameError, SyntaxError):
            pass
        setattr(instance, attr_name, attr_value)
        instance.save

    def do_help(self, arg):
        """
        Display help information.


        Attributes:
            arg (str): show the infomation about the commands.


          """
        if arg:
            try:
                func = getattr(self, 'help_' + arg)
                func()
            except AttributeError:
                print(f"No help available for {arg}")
        else:
            cmd.Cmd.do_help(self, arg)

    def help_quit(self):
        """
        Help information for quit command.
        """
        print("Quit command to exit the program.")
        print()

    def help_EOF(self):
        """
        Help information for EOF command.
        """
        print("EOF command to exit the program.")

    def help_help(self):
        """
        Help information for help command.
        """
        print("List available commands with 'help'")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
