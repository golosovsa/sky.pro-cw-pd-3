"""
    Coursework №3
    Golosov_SA aka grm
    link: https://skyengpublic.notion.site/3-d2893a166cf0479a8c8bb3bfb13d478e#70281dd53e6e4930843e2501562a72f2

    Views from search blueprint
"""

# global imports
from flask import Blueprint, render_template, request
from werkzeug.exceptions import NotFound, InternalServerError, HTTPException
import logging

# local imports
from .model import Search


search = Blueprint("search", __name__, template_folder="templates")


# Loggers
log_user_activity = logging.getLogger("user")
# log_api_usage = logging.getLogger("api")
log_errors = logging.getLogger("errors")


@search.route("/", methods=["GET"])
def search_index():
    """ Search index view """

    log_user_activity.info(str(request))

    try:
        substring = request.args.get("s", None)

        if substring is None:
            raise NotFound()

        search_page = Search(substring)

        return render_template("search.html", search_page=search_page)

    except (TypeError, ValueError, KeyError, OSError) as e:
        log_errors.error(str(e))
        raise InternalServerError()

    except HTTPException as e:
        log_errors.error(str(e))
        raise e
