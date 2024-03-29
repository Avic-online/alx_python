#!/usr/bin/python3
# model state script

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

# this is he class state that is inherited from Base
class State(Base):
    # this is he class state that is inherited from Base
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)