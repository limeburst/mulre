""":mod:`mulre.yarn` --- Yarn
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

"""
from sqlalchemy.orm import relationship
from sqlalchemy.sql.functions import now
from sqlalchemy.schema import Column
from sqlalchemy.types import Integer, DateTime
from sqlalchemy.dialects.postgres import INET

from .orm import Base


class User(Base):
    id = Column(Integer, primary_key=True)
    yarns = relationship('Yarn')
    remote_addr = Column(INET, nullable=False)
    created_at = Column(DateTime(timezone=True), nullable=False, default=now())

    __tablename__ = 'users'
