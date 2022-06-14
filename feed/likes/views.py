"""
    Coursework №3
    Golosov_SA aka grm
    link: https://skyengpublic.notion.site/3-d2893a166cf0479a8c8bb3bfb13d478e#70281dd53e6e4930843e2501562a72f2

    Views from likes blueprint
"""

# global imports
from flask import Blueprint, redirect, url_for, request
from werkzeug.exceptions import InternalServerError, NotFound, HTTPException
import logging

# local imports
from .model import LikesApi


likes = Blueprint("likes", __name__, template_folder="templates")


# Loggers
log_user_activity = logging.getLogger("user")
# log_api_usage = logging.getLogger("api")
log_errors = logging.getLogger("errors")


@likes.route("/add/<int:post_id>")
def likes_index(post_id):
    """ Likes index api view """

    log_user_activity.info(str(request))

    try:
        likes_api = LikesApi(post_id)

        if likes_api.post is None:
            raise NotFound()

        return redirect(url_for("feed.posts.posts_index", post_id=post_id), code=302)

    except (TypeError, KeyError, ValueError, OSError) as e:
        log_errors.error(str(e))
        raise InternalServerError()

    except HTTPException as e:
        log_errors.error(str(e))
        raise e


