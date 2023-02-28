#!/usr/bin/python3
'''Store first objects'''
import json
from models.base_model import BaseModel

class FileStorage:
    '''Serializes and deserializes file'''
    __file_path = "file.json"
    __objects = {}

    def all(self):
        '''return dictionarty objects'''
        return FileStorage.__objects

    def new(self, obj):
        '''sets in __objects the obj with key <classname>.id'''
        cls_name = type(obj).__name__
        key = cls_name + "." + obj.id
        FileStorage.__objects[key] = obj

    def save(self):
        '''to the JSON file'''
        my_obj = {}
        for k, v in FileStorage.__objects.items():
            my_obj[k] = v.to_dict()
        json.dump(my_obj, fp)

    def reload(self):
        '''to python objs'''
        try:
            with open(FileStorage.__file_path, 'r', encoding="utf-8") as fp:
                obj_dict = json.load(fp)
                for k, v in obj_dict.items():
                    cls_name = v['__class__']
                    obj = eval(cls_name)(**v)
                    key = cls_name + "." + v['id']
                    FileStorage.__objects[key] = obj
        except FileNotFoundError:
            pass
            return
