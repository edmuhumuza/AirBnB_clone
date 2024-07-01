#!/usr/bin/python3
"""
Documentation for the console module in alx school is comming soon.
"""
import cmd
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review

class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb) '

    def precmd(self, arg):
        if '.' in arg :
            if arg.endswith('()'):
                arg = arg.split('.')
                class_name = arg[0]
                command = arg[1].replace('(','').replace(')','')
                line = command + " " + class_name
                return line
            elif '{' in arg and '}' in arg:
                arg = arg.split('.', 1)
                class_name = arg[0]
                arg = arg[1].split('(', 1)
                command = arg[0]
                arg = arg[1].replace('"','', 2).replace(')','')
                arg = arg.split(',',1)
                inst_id = arg[0]
                dict_rep = arg[1]
                line = command + " " + class_name + " " + inst_id + " " + dict_rep
                print("in precmd" + line)
                return line

            else:
                arg = arg.split('.')
                class_name = arg[0]
                arg = arg[1].split('(')
                command = arg[0]
                inst_id = arg[1].replace('"','').replace(')','').replace(',','')
                line = command + " " + class_name + " " + inst_id
                return line
        else:
            return arg

    def do_all(self, arg):
        if arg:
            if arg and arg not in ['BaseModel', 'User', 'Place', 'State', 'City', 'Amenity', 'Review']:
                print('** class doesn\'t exist **')
                return
            from models.__init__ import storage
            iter_dict = storage.all()
            ret_list = []
            for k,v in iter_dict.items():
                if type(v).__name__ == arg:
                    ret_list.append(str(v))
            print(ret_list)
        else:
            from models.__init__ import storage
            iter_dict = storage.all()
            ret_list = []
            for k,v in iter_dict.items():
                ret_list.append(str(v))
            print(ret_list)
    def do_count(self, arg):
        if arg:
            if arg and arg not in ['BaseModel', 'User', 'Place', 'State', 'City', 'Amenity', 'Review']:
                print('** class doesn\'t exist **')
                return
            from models.__init__ import storage
            iter_dict = storage.all()
            ret_list= []
            for k,v in iter_dict.items():
                if type(v).__name__ == arg:
                    ret_list.append(str(v))
            print(len(ret_list))
        else:
            pass

    def do_create(self, class_name):
        if not class_name:
            print('** class name missing **')
        if class_name and class_name not in ['BaseModel', 'User', 'Place', 'State', 'City', 'Amenity', 'Review']:
            print('** class doesn\'t exist **')
        if class_name and class_name in ['BaseModel', 'User','Place', 'State', 'City', 'Amenity', 'Review']:
            from models.base_model import BaseModel
            from models.user import User
            from models.amenity import Amenity
            new_instance = eval(class_name + '()')
            new_instance.save()
            print(new_instance.id)
    def do_show(self, arg):
        args = arg.split()
        if not args:
            print('** class name is missing **')
            return
        if args[0] and args[0] not in ['BaseModel', 'User' , 'Place', 'State', 'City', 'Amenity', 'Review']:
            print('** class doesn\'t exist **')
            return
        if len(args) < 2:
            print('** instance id missing **')
            return
        if len(args) == 2:
            from models.__init__ import storage
            from models.user import User
            check_key = f"{args[0]}.{args[1]}"
            my_dict = storage.all()
            if check_key not in my_dict.keys():
                print('** no instance found **')
                return
            for k, v in my_dict.items():
                if k == check_key:
                    value = my_dict[k].to_dict()
                    print(value)
                    return
    def do_update(self, line):
        args = line.split()
        if not line:
            print('** class name missing **')
            return
        if args[0] not in ['BaseModel', 'User', 'Place', 'State', 'City', 'Amenity', 'Review']:
            print('** class doesn\'t exist **')
            return
        if len(args) < 2:
            print('** instance id missing **')
            return
        if args[1]:
            from models.__init__ import storage
            from models.user import User
            check_key = f"{args[0]}.{args[1]}"
            my_dict = storage.all()
            if check_key not in my_dict.keys():
                print('** no instance found **')
                return
        if len(args) < 3:
            print('** attribute name missing **')
            return
        if len(args) < 4:
            print('** value missing **')
            return 
        if '{' in line and '}' in line:
            from models.__init__ import storage
            args = line.split(maxsplit=2)
            print(args)
            from models.city import City
            v_dict = eval(str(args[2]))
            if 'created_at' in v_dict.keys() or 'id' in v_dict.keys() or 'updated_at' in v_dict.keys():
                print("Can\'t update")
                return
            check_key = f"{args[0]}.{args[1]}"
            my_dict = storage.all()[check_key]
            for key,value in v_dict.items():
                setattr(my_dict, key, value)
            storage.save()
        else:
            from models.__init__ import storage
            from models.user import User
            check_key = f"{args[0]}.{args[1]}"
            my_dict = storage.all()
            for k,v in my_dict.items():
                if k == check_key:
                    attr = args[2].replace('"','').replace("'",'')
                    val = args[3].replace('"','').replace("'",'')
                    setattr(my_dict[k], attr, val)
            storage.save()

    def do_destroy(self, arg):
        args = arg.split()
        if not args:
            print('** class name is missing **')
            return
        if args[0] not in ['BaseModel', 'User', 'Place', 'State', 'City', 'Amenity', 'Review']:
            print('** class doesn\'t exist **')
            return
        if len(args) < 2:
            print('** instance id missing **')
            return
        if args[1]:
            from models.__init__ import storage
            check_key = f"{args[0]}.{args[1]}"
            my_dict = storage.all()
            if check_key not in my_dict.keys():
                print('** no instance found **')
                return
        if args:
            from models.__init__ import storage
            from models.user import User
            class_id = f"{args[0]}.{args[1]}"
            
            storage.delete(class_id)
            storage.save()
            return
    def do_quit(self, line):
        return True
    def do_EOF(self, line):
        print()
        return True
    def help_quit(self):
        print('Quit command to exit the program')
        print()
        print()
    def help_EOF(self):
        print('EOF command to exit the program')
        print()
        print()
    def emptyline(self):
        pass
if __name__ == '__main__':
    HBNBCommand().cmdloop()
