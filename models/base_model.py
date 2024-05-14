#!/usr/bin/python3
"""
"""
import uid
from datetime import datetime

class BaseModel:
    def __init__(sel):
        self.id = str(uuid.uuid4())

        self.created = datetime.utcnow()

    def save(self):
        """
        """
        self.updated_at = datetime.utcnow

    def to_dict(self):
        """
        """
        inst_dict = self.__dict__.copy()
        inst_dict["__class__"] = self.__class__.name__
        inst_dict["created_at"] = self.created_at.isoformat()
        inst_dict["updated_at"] = self.updated_at.isoformat()

        return inst_dict
    def __str__(self):
        """
        """
        class_name = self.__class__.name__
        return "[{}] [{}] {}".format(class_name, self.id, self.__dict__)

if __name__ = "__main__":
    my_Model = BaseModel()
    My_Model.name = "My first model"
    My_Model.my_number = 89
    print(my_model)
    my_model.save()
    print(my_model)
    my_model_json = my_model.to_dict()
    print(my_model_json)
    print("JSON Of my node:")
    for key in my_model_json.key():
        print("\t{}: ({} - {}".format(key, type(my_model_json[key]). my_model_json[key])):
