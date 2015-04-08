""":mod:`mulre.web.user` --- User pages
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

"""
from flask import Blueprint, render_template

from ..yarn import User, Yarn
from .tag import get_random_tags
from .db import session


bp = Blueprint('user', __name__)


def get_user(remote_addr):
    user = session.query(User).filter_by(remote_addr=remote_addr).first()
    return user


@bp.route('/')
def home():
    """Home."""
    yarns = session.query(Yarn).order_by(Yarn.id).all()
    tags = get_random_tags()
    return render_template('home.html', yarns=yarns, tags=tags)
