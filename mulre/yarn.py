""":mod:`mulre.yarn` --- Yarn
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

"""
import boto3
from botocore.client import Config
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
        return '{}/{}.{}'.format(self.__tablename__, self.id,
                                 self.filename.rsplit('.', 1)[1])

    def from_blob(self, blob):
        s3 = boto3.resource('s3')
        o = s3.Object(current_app.config['AWS_S3_BUCKET'], self.key)
        return o.put(Body=blob)

    def get_url(self):
        if self.filename:
            s3 = boto3.client('s3', config=Config(signature_version='s3v4'))
            return s3.generate_presigned_url(
                ClientMethod='get_object',
                Params={
                    'Bucket': current_app.config['AWS_S3_BUCKET'],
                    'Key': self.key,
                }
            )
        else:
            return None

    __tablename__ = 'yarns'


class Tag(Base):
    id = Column(Integer, primary_key=True)
    name = Column(UnicodeText, nullable=False, unique=True)

    __tablename__ = 'tags'
