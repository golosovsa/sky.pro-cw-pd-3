"""
    Coursework №3
    Golosov_SA aka grm
    link: https://skyengpublic.notion.site/3-d2893a166cf0479a8c8bb3bfb13d478e#70281dd53e6e4930843e2501562a72f2

    Views from api blueprint
"""

# global imports
from flask import Blueprint, jsonify, request, url_for
from werkzeug.exceptions import InternalServerError, HTTPException
import logging

# local imports
from .model import ApiPost

# The Api Blueprint
api = Blueprint("api", __name__, template_folder="template")

# Loggers
# log_user_activity = logging.getLogger("user")
log_api_usage = logging.getLogger("api")
log_errors = logging.getLogger("errors")


@api.route("/posts")
def api_posts_index():
    """ Get all posts api handle view """

    log_api_usage.info(str(request))

    try:
        api_post = ApiPost()
        data = api_post.get_all()

    except (TypeError, KeyError, ValueError, OSError) as e:
        log_errors.error(str(e))
        raise InternalServerError()

    return jsonify(data), 200


@api.route("/posts/<int:post_id>")
def api_post_index(post_id):
    """ Get a post api handle view """

    log_api_usage.info(str(request))

    try:
        api_post = ApiPost()
        data = api_post.get_one(post_id)

    except (IndexError, TypeError, KeyError, ValueError, OSError) as e:
        log_errors.error(str(e))
        data = None

    except HTTPException as e:
        log_errors.error(str(e))
        data = None

    return jsonify(data), 200


@api.route("/")
def api_usage():
    return f"<h1>Hello from API</h1>\n" \
           f"<h2>USAGE:</h2>" \
           f"<p>If not exists returns null</p>\n" \
           f"<p>Use endpoints:</p>\n" \
           f"<p>{url_for('api.api_posts_index')}</p>\n" \
           f"<p>{url_for('api.api_post_index', post_id=1)} [2, 3, 4, ...]</p>", 200


@api.errorhandler(HTTPException)
def api_error_handle(e):
    return "null", 200
