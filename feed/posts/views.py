"""
    Coursework №3
    Golosov_SA aka grm
    link: https://skyengpublic.notion.site/3-d2893a166cf0479a8c8bb3bfb13d478e#70281dd53e6e4930843e2501562a72f2

    Views from posts blueprint
"""

# global imports
from flask import Blueprint, render_template, request
from werkzeug.exceptions import InternalServerError, NotFound, HTTPException
import logging

# local imports
from .model import Post


posts = Blueprint("posts", __name__, template_folder="templates")


# Loggers
log_user_activity = logging.getLogger("user")
# log_api_usage = logging.getLogger("api")
log_errors = logging.getLogger("errors")


@posts.route("/<int:post_id>")
def posts_index(post_id):
    """ Posts index view """

    log_user_activity.info(str(request))

    try:
        post_page = Post(post_id)

        if post_page.post is None:
            raise NotFound()

        return render_template("post.html", post_page=post_page)

    except (TypeError, ValueError, KeyError, OSError) as e:
        log_errors.error(str(e))
        raise InternalServerError()

    except HTTPException as e:
        log_errors.error(str(e))
        raise e

