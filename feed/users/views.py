"""
    Coursework №3
    Golosov_SA aka grm
    link: https://skyengpublic.notion.site/3-d2893a166cf0479a8c8bb3bfb13d478e#70281dd53e6e4930843e2501562a72f2

    Views from users blueprint
"""

# global imports
from flask import Blueprint, render_template, request
from werkzeug.exceptions import InternalServerError, HTTPException, NotFound
import logging

# local imports
from .model import Users


users = Blueprint("users", __name__, template_folder="templates")


# Loggers
log_user_activity = logging.getLogger("user")
# log_api_usage = logging.getLogger("api")
log_errors = logging.getLogger("errors")


@users.route("/<username>")
def users_index(username):
    """ Users index view """

    log_user_activity.info(str(request))

    try:
        users_page = Users(username)

        if not users_page.posts:
            raise NotFound()

        return render_template("user-feed.html", users_page=users_page)

    except (TypeError, ValueError, KeyError, OSError) as e:
        log_errors.error(str(e))
        raise InternalServerError()

    except HTTPException as e:
        log_errors.error(str(e))
        raise e
