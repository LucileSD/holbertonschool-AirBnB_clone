#!/usr/bin/python3
"""
    import modules
"""
from datetime import datetime
import uuid
import models


class BaseModel:
    """
        base class for an instance
    """
    def __init__(self, *args, **kwargs):
        """
            initiate the id of an instance with the date time
            args:
                args: set of unnamed arguments
                kwargs: the set of arguments named
        """
        if len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                if key != "__class__":
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """
            returns a string with the information of the object
        """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """
            updates the public instance attribute
            updated_at with the current datetime
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
            returns a dictionary containing all keys/values of
            __dict__ of the instance
        """
        dict = {"__class__": self.__class__.__name__}
        for key, value in self.__dict__.items():
            if key in ["created_at", "updated_at"]:
                dict[key] = value.isoformat()
            else:
                dict[key] = value
        return dict
