""":mod:`mulre.web.tag` --- Tag pages
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

"""
from flask import Blueprint, redirect, render_template, url_for
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
    random_tags = get_random_tags()
    all_tags = session.query(Tag).filter(Tag.yarns.any()).order_by(Tag.name).all()
    return render_template('tags.html', random_tags=random_tags, all_tags=all_tags)


@bp.route('/random/')
def random():
    random_tags = get_random_tags(1)
    if random_tags:
        return redirect(url_for('tag.yarns', tag_name=random_tags[0].name))
    else:
        return redirect(url_for('user.home'))


@bp.route('/<tag_name>/')
def yarns(tag_name):
    random_tags = get_random_tags()
    tag = session.query(Tag).filter_by(name=tag_name).first()
    return render_template('tag.html', random_tags=random_tags, tag=tag)
