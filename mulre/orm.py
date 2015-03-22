""":mod:`mulre.orm` --- Object-relational mapping
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

"""
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


#: SQLAlchemy declarative base class.
Base = declarative_base()

#: SQLAlchemy session class.
Session = sessionmaker()
