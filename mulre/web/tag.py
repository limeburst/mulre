""":mod:`mulre.web.tag` --- Tag pages
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

"""
from flask import Blueprint, render_template
from sqlalchemy.sql import func

from ..yarn import Tag
from .db import session


bp = Blueprint('tag', __name__)


def get_random_tags(count=5):
    tags = session.query(Tag) \
                  .filter(Tag.yarns.any()) \
                  .order_by(func.random()) \
                  .limit(count) \
                  .all()
    return tags


@bp.route('/')
def tags():
    tags = session.query(Tag).filter(Tag.yarns.any()).order_by(Tag.name).all()
    return render_template('tags.html', tags=tags)


@bp.route('/<tag_name>/')
def yarns(tag_name):
    tags = get_random_tags()
    tag = session.query(Tag).filter_by(name=tag_name).first()
    return render_template('tag.html', tags=tags, tag=tag)
