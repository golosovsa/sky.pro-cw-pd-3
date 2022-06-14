"""
    Coursework №3
    Golosov_SA aka grm
    link: https://skyengpublic.notion.site/3-d2893a166cf0479a8c8bb3bfb13d478e#70281dd53e6e4930843e2501562a72f2

    Views from tag blueprint
"""

# global imports
from flask import Blueprint, render_template, request
from werkzeug.exceptions import InternalServerError, NotFound, HTTPException
import logging

# local imports
from .model import Tag

tag = Blueprint("tag", __name__, template_folder="templates")


# Loggers
log_user_activity = logging.getLogger("user")
# log_api_usage = logging.getLogger("api")
log_errors = logging.getLogger("errors")


@tag.route("/<tag_name>")
def tag_index(tag_name):
    """ Tag index view """

    log_user_activity.info(str(request))

    try:
        tag_page = Tag(tag_name)

        if len(tag_page.posts) == 0:
            raise NotFound()

        return render_template("tag.html", tag_page=tag_page)

    except (TypeError, ValueError, KeyError, OSError) as e:
        log_errors.error(str(e))
        raise InternalServerError()

    except HTTPException as e:
        log_errors.error(str(e))
        raise e


