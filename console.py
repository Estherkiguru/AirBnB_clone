#!/usr/bin/python3
"""module that defines the command line console"""
import cmd
from models import storage
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "
    valid_classes = ["BaseModel"]

    def do_quit(self, arg):
        """Quit command to exit the program\n"""
        return True

    def do_EOF(self, arg):
        """Quit command to exit the program\n"""
        print()
        return True
    
    def emptyline(self):
        """Handles an empty line input\n"""
        pass

    @staticmethod
    def __check_args(arg):
        """
        Performing the prerequisite checks on the type and number of
        arguments passed
        Returns: classname
        """
        if arg is None:
            print("** class name missing **")
            return None
        try:
            cls_name = globals()[arg]
            return cls_name
        except KeyError:
            print("** class doesn't exist **")

    def do_create(self, arg):
        """
        Handles creating new instances of Basemodel
        Saves it to JSON file
        Print ID of created instances
        Usage: (hbnb) create <class_name>
        """
        cls_name = HBNBCommand.__check_args(arg)
        if cls_name:
            new_instance = cls_name()
            new_instance.save()
            print(new_instance.id)
        
    def do_show(self, arg):
        """
        print string representation of an instance
        Usage: (hbnb) show <class_name> <object_id>
        """
        cmd_args = list(arg.split(" "))
        cls_name = HBNBCommand.__check_args(cmd_args[0])
        if cls_name and len(cmd_args) < 2:
            print("** instance id missing **")
        elif cls_name:
            all_objects = storage.all()
            for key, obj in all_objects.items():
                name, obj_id = key.split(".")
                if obj_id == cmd_args[1]:
                    print(obj)  #: Will implicitly call the dunder str
                    return
            print("** no instance found **")

    def do_all(self, arg):
        """
        Prints string representation of all instances
        """
        all_objects = storage.all()
        cmd_args = list(arg.split(" "))
        obj_list = []
        if len(cmd_args) == 0:
            for key, value in all_objects.items():
                obj_list.append(str(value))
            print(obj_list)
        elif cmd_args[0] not in self.valid_classes:
            print("** class doesn't exist **")
        else:
            for key, value in all_objects.items():
                if key.split(".")[0] == cmd_args[0]:
                    obj_list.append(str(value))
            print(obj_list)
            
    def do_destroy(self, arg):
        """
        Handles deletion of an instance
        Changes saved to JSON file
        Usage: (hbnb) destroy <class_name> <object_id>
        """
        cmd_args = list(arg.split(" "))
        cls_name = HBNBCommand.__check_args(cmd_args[0])
        if cls_name and len(cmd_args) < 2:
            print("** instance id missing **")
        elif cls_name:
            all_objects = storage.all()
            ll_objects = storage.all()
            for key, obj in all_objects.items():
                name, obj_id = key.split(".")
                if obj_id == cmd_args[1]:
                    del all_objects[key]
                    storage.save()
                    return
            print("** no instance found **")

    def do_update(self, arg):
        """
        Updates instances based on cass name and id
        Usage:Update <class_name> <id> <attribute_name> "<attribute_value>"
        """
        cmd_args = list(arg.split(" "))
        # Verify the validity of the class_name argument
        cls_name = HBNBCommand.__check_args(cmd_args[0])
        if cls_name:
            if len(cmd_args) < 2:
                print("** instance id missing **")
            elif len(cmd_args) < 3:
                print("** attribute name missing **")
            elif len(cmd_args) < 4:
                print("** value missing **")
            elif len(cmd_args) > 3:
                # Extract the saved existing instances
                all_objects = storage.all()
                # Parse that dictionary to get the exact instance by id
                for key, obj in all_objects.items():
                    obj_id = key.split(".")[1]
                    if cmd_args[1] == obj_id:
                # Update the actual instance dictionary
                        setattr(obj, cmd_args[2], cmd_args[3])
                # Save the changes
                        obj.save()
                        return
                print("** no instance found **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
