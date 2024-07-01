#!/usr/bin/python3
"""BaseModel base class that defines all common attributes/methods for other classes."""
import uuid
import datetime
from models import storage
class BaseModel():
    def __init__(self, *args, **kwargs):
        if kwargs:
            for k,v in kwargs.items():
                if k != '__class__':
                    if k == 'created_at':
                        setattr(self, k, datetime.datetime.fromisoformat(v))
                    elif k == 'updated_at':
                        setattr(self, k, datetime.datetime.fromisoformat(v))
                    else:
                        setattr(self, k, v)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.now()
            self.updated_at = datetime.datetime.now()
        storage.new(self)

    def __str__(self):
        a = str(type(self).__name__)
        b = str(self.id)
        c = str(self.__dict__)
        return  "[" + a + "]" + " " + "(" + b + ")" + " " + c
    

    def save(self):
        self.updated_at = datetime.datetime.now()

    def to_dict(self):
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict

