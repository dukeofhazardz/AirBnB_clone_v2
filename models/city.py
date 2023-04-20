#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel
<<<<<<< HEAD
from models.base_model import Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
=======
>>>>>>> parent of 95603be (Updated and improved do_created and set up datatbases)


class City(BaseModel):
    """ The city class, contains state ID and name """
<<<<<<< HEAD
    __tablename__ = "cities"
    name = Column(String(128), nullable=False)
    state_id = Column(String(60), ForeignKey("states.id"), nullable=False)
    places = relationship("Place", backref="cities", cascade="delete")
=======
    state_id = ""
    name = ""
>>>>>>> parent of 95603be (Updated and improved do_created and set up datatbases)
