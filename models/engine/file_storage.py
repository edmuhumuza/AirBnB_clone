#!/usr/bin/python3
import json
import os

class FileStorage():
    __file_path = 'file.txt'
    __objects = {}

    def all(self):
        return FileStorage.__objects
    
    def new(self, obj):
        FileStorage.__objects[f"{type(obj).__name__}.{obj.id}"] = obj

    def save(self):
        all_objs = FileStorage.__objects

        obj_dict = {}

        for obj in all_objs.keys():
            obj_dict[obj] = all_objs[obj].to_dict()

        with open(FileStorage.__file_path, 'w', encoding='utf-8') as file:
            json.dump(obj_dict, file)

    def reload(self):
        if os.path.isfile(FileStorage.__file_path):
            try:
                with open(FileStorage.__file_path, 'r', encoding='utf-8') as file:
                    from models.base_model import BaseModel
                    from models.user import User
                    from models.place import Place
                    from models.state import State
                    from models.city import City
                    from models.amenity import Amenity
                    from models.review import Review
                    obj_dict = json.load(file)
                    for key, value in obj_dict.items():
                        clas = value["__class__"]
                        obj = eval(clas + "(**value)")
                        FileStorage.__objects[key] = obj
            except Exception as e:
                pass
    def delete(self, class_id):
        inst_dict = dict(FileStorage.__objects)
        for k,v in inst_dict.items():
            if k == class_id:
                del FileStorage.__objects[k]
