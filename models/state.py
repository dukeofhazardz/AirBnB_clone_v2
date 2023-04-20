#!/usr/bin/python3
""" State Module for HBNB project """
<<<<<<< HEAD
from os import getenv
import models
from models.base_model import BaseModel
from models.base_model import Base
from models.city import City
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
=======
from models.base_model import BaseModel
>>>>>>> parent of 95603be (Updated and improved do_created and set up datatbases)


class State(BaseModel):
    """ State class """
    name = ""
