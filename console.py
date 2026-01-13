#!/usr/bin/python3
"""Console module - command interpreter for AirBnB clone"""
import cmd
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """HBNBCommand class - command interpreter"""

    prompt = '(hbnb) '
    valid_classes = [
        'BaseModel', 'User', 'State', 'City', 'Amenity', 'Place', 'Review'
    ]

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program"""
        print()
        return True

    def emptyline(self):
        """Do nothing on empty line"""
        pass

    def do_create(self, arg):
        """Create new instance of a class, save it, and print id
        Usage: create <class name>
        """
        if not arg:
            print("** class name missing **")
            return

        args = arg.split()
        class_name = args[0]

        if class_name not in self.valid_classes:
            print("** class doesn't exist **")
            return

        new_instance = eval(class_name)()
        new_instance.save()
        print(new_instance.id)

    def do_show(self, arg):
        """Print string representation of instance based on class name and id
        Usage: show <class name> <id>
        """
        if not arg:
            print("** class name missing **")
            return

        args = arg.split()
        class_name = args[0]

        if class_name not in self.valid_classes:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        obj_id = args[1]
        key = f"{class_name}.{obj_id}"
        objects = storage.all()

        if key not in objects:
            print("** no instance found **")
            return

        print(objects[key])

    def do_destroy(self, arg):
        """Delete instance based on class name and id
        Usage: destroy <class name> <id>
        """
        if not arg:
            print("** class name missing **")
            return

        args = arg.split()
        class_name = args[0]

        if class_name not in self.valid_classes:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        obj_id = args[1]
        key = f"{class_name}.{obj_id}"
        objects = storage.all()

        if key not in objects:
            print("** no instance found **")
            return

        del objects[key]
        storage.save()

    def do_all(self, arg):
        """Print string representation of all instances or all of a class
        Usage: all [class name]
        """
        objects = storage.all()
        obj_list = []

        if not arg:
            for obj in objects.values():
                obj_list.append(str(obj))
        else:
            class_name = arg.split()[0]
            if class_name not in self.valid_classes:
                print("** class doesn't exist **")
                return

            for key, obj in objects.items():
                if key.startswith(class_name + '.'):
                    obj_list.append(str(obj))

        print(obj_list)

    def do_update(self, arg):
        """Update instance by adding or updating attribute
        Usage: update <class name> <id> <attribute name> "<attribute value>"
        """
        if not arg:
            print("** class name missing **")
            return

        args = arg.split()

        if args[0] not in self.valid_classes:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        class_name = args[0]
        obj_id = args[1]
        key = f"{class_name}.{obj_id}"
        objects = storage.all()

        if key not in objects:
            print("** no instance found **")
            return

        if len(args) < 3:
            print("** attribute name missing **")
            return

        if len(args) < 4:
            print("** value missing **")
            return

        obj = objects[key]
        attr_name = args[2]
        attr_value = args[3].strip('"')

        # Don't update id, created_at, updated_at
        if attr_name in ['id', 'created_at', 'updated_at']:
            return

        # Cast value to appropriate type
        if hasattr(obj, attr_name):
            attr_type = type(getattr(obj, attr_name))
            try:
                attr_value = attr_type(attr_value)
            except (ValueError, TypeError):
                pass

        setattr(obj, attr_name, attr_value)
        obj.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
