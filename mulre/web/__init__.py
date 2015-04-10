""":mod:`mulre.web` --- Mulre web
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

"""
from flask import Flask

from . import tag, user, yarn
from .db import setup_session
from .util import MethodRewriteMiddleware


def create_app(config):
    """The application factory.

    :param config: The instance relative configuration file to use.
    :returns: A Mulre Flask app.
    :rtype: :class:`flask.Flask`

    """
    app = Flask(__name__, instance_relative_config=True)
    app.wsgi_app = MethodRewriteMiddleware(app.wsgi_app)
    app.config.from_pyfile(config)
    setup_session(app)
    app.register_blueprint(user.bp)
    app.register_blueprint(tag.bp, url_prefix='/tags')
    app.register_blueprint(yarn.bp, url_prefix='/yarns')
    return app
