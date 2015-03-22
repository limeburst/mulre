""":mod:`mulre.yarn` --- Yarn
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

"""
from boto.s3.connection import S3Connection
from boto.s3.key import Key
from flask import current_app
from sqlalchemy.orm import relationship
from sqlalchemy.schema import Column, ForeignKey, Table
from sqlalchemy.sql.functions import now
from sqlalchemy.types import DateTime, Integer, UnicodeText, Unicode

from .orm import Base
from .user import User


tagging = Table('tagging', Base.metadata,
                Column('tag_id', Integer, ForeignKey('tags.id')),
                Column('yarn_id', Integer, ForeignKey('yarns.id'))
                )


class Yarn(Base):
    id = Column(Integer, primary_key=True)
    content = Column(UnicodeText, nullable=False)
    created_at = Column(DateTime(timezone=True), nullable=False, default=now())
    filename = Column(Unicode, default=None)
    author_id = Column(Integer, ForeignKey(User.id), nullable=False)
    author = relationship('User')
    tags = relationship('Tag', secondary=tagging, backref='yarns')

    @property
    def key(self):
        config = current_app.config
        c = S3Connection(config['AWS_ACCESS_KEY_ID'], config['AWS_SECRET_KEY'])
        b = c.get_bucket(config['AWS_S3_BUCKET'], validate=False)
        k = Key(b)
        k.key = '{}/{}.{}'.format(self.__tablename__, self.id,
                                  self.filename.rsplit('.', 1)[1])
        return k

    def from_blob(self, blob):
        return self.key.set_contents_from_string(blob)

    def get_url(self, expires_in=300):
        return self.key.generate_url(expires_in)

    __tablename__ = 'yarns'


class Tag(Base):
    id = Column(Integer, primary_key=True)
    name = Column(UnicodeText, nullable=False, unique=True)

    __tablename__ = 'tags'
