""":mod:`mulre.web.stream` --- Streaming endpoints
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

"""
from flask import Blueprint, Response, stream_with_context

from .redis import redis


bp = Blueprint('stream', __name__)


@bp.route('/firehose/')
def firehose():
    def generate():
        pubsub = redis.pubsub()
        pubsub.subscribe('firehose')
        for event in pubsub.listen():
            if event['type'] == 'message':
                yield 'data: {}\r\n\r\n'.format(event['data'].decode('utf-8')).encode('utf-8')
    return Response(stream_with_context(generate()),
                    direct_passthrough=True,
                    mimetype='text/event-stream')
