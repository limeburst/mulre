""":mod:`mulre.web.redis` --- Redis connections
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Use :data:`redis` in view functions.

"""
from __future__ import absolute_import

from flask import current_app, g
from redis import Redis
from werkzeug.local import LocalProxy


def get_redis():
    """Gets a Redis connection.  If there's none yet, creates one.

    :returns: A Redis connection
    :rtype: :class:`redis.Redis`

    """
    if not hasattr(g, 'redis'):
        g.redis = Redis(host=current_app.config['REDIS_URL'])
    return g.redis


#: (:class:`~werkzeug.local.LocalProxy` of :class:`~favien.orm.Session`)
#: The context local session. Use this.
redis = LocalProxy(get_redis)
