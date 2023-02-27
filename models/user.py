#!/usr/bin/python3
'''create a class user'''

from models.base_model import BaseModel

class User(BaseModel):
    '''Define a user'''
    def __init__(self):
        self.email = ""
        self.password = ""
        self.first_name = ""
        self.last_name = ""