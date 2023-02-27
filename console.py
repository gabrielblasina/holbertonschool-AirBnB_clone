#!/usr/bin/python3
"""Console"""


import cmd

from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """class called HBNB wich creates custom prompt for the interpreter"""

    prompt = '(hbnb) '

    def do_quit(self, arg):
        """Quit command to exit the program"""

        return True

    def do_EOF(self, arg):
        """exits the program when EOF is executed"""

        print()
        return True

    def emptyline(self):
        """do nothing when empty line + ENTER are executed"""

        pass

    def help_quit(self):
        """Print help message for quit command"""

        print("Quit command to exit the program.")
        print()

    def do_create(self, line_args):
        """ Creates a new instance, prints id and saves to json """

        split_args = line_args.split()
        if len(split_args) < 1:
            print("** class name missing **")
        elif split_args[0] == "BaseModel":
            new_instance = BaseModel()
            new_instance.save()
            print(new_instance.id)
        else:
            print("** class doesn't exist **")

    def do_show(self, line_args):
        """ prints the string representation of an instance """

        split_args = line_args.split()
        if len(split_args) < 1:
            print("** class name missing **")
        elif split_args[0] == "BaseModel" and len(split_args) < 2:
            print("** instance id missing **")
        elif split_args[0] != "BaseModel":
            print("** class doesn't exist **")
        elif f"BaseModel.{split_args[1]}" in storage.all().keys():
            usable_dict = storage.all()
            print(usable_dict[f"BaseModel.{split_args[1]}"])
        else:
            print("** no instance found **")

    def do_destroy(self, line_args):
        """ destroys the specified object """

        split_args = line_args.split()
        if len(split_args) < 1:
            print("** class name missing **")
        elif split_args[0] == "BaseModel" and len(split_args) < 2:
            print("** instance id missing **")
        elif split_args[0] != "BaseModel":
            print("** class doesn't exist **")
        elif f"BaseModel.{split_args[1]}" in storage.all().keys():
            del storage.all()[f"BaseModel.{split_args[1]}"]
            storage.save()
        else:
            print("** no instance found **")

    def do_all(self, line_args):
        """ prints all string representation of all instances """

        split_args = line_args.split()
        if len(split_args) < 1:
            print([f"{str(val)}" for val in storage.all().values()])
        elif split_args[0] == "BaseModel":
            print([f"{str(val)}" for val in storage.all().values()])
        elif split_args[0] != "BaseModel":
            print("** class doesn't exist **")

    def do_update(self, line_args):
        """ updates an instance by chaning attribute """

        split_args = line_args.split()
        if len(split_args) < 1:
            print("** class name missing **")
        elif split_args[0] != "BaseModel":
            print("** class doesn't exist **")
        elif len(split_args) < 2:
            print("** instance id missing **")
        elif f"BaseModel.{split_args[1]}" not in storage.all().keys():
            print("** no instance found **")
        elif len(split_args) < 3:
            print("** attribute name missing **")
        elif len(split_args) < 4:
            print("** value missing **")
        else:
            if split_args[3].isdigit():
                casted_arg = int(split_args[3])
            elif split_args[3].count(".") == 1:
                if not split_args[3].endswith(".") and not\
                   split_args[3].startswith("."):
                    if split_args[3].replace(".", "2").isdigit():
                        casted_arg = float(split_args[3])
                    else:
                        casted_arg = str(split_args[3])
                else:
                    casted_arg = str(split_args[3])
            else:
                casted_arg = str(split_args[3])
            if type(casted_arg) is str:
                if casted_arg.startswith('"') and casted_arg.endswith('"') and\
                   casted_arg.count('"') % 2 == 0:
                    casted_arg = casted_arg[1:len(casted_arg) - 1]
                if casted_arg.startswith("'") and casted_arg.endswith("'") and\
                   casted_arg.count("'") % 2 == 0:
                    casted_arg = casted_arg[1:len(casted_arg) - 1]
            setattr(storage.all()[f"BaseModel.{split_args[1]}"],
                    split_args[2], casted_arg)
            storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
