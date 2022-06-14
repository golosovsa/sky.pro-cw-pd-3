"""
    Coursework №3
    Golosov_SA aka grm
    link: https://skyengpublic.notion.site/3-d2893a166cf0479a8c8bb3bfb13d478e#70281dd53e6e4930843e2501562a72f2

    Views from bookmarks blueprint
"""

# global imports
from flask import Blueprint, render_template, redirect, url_for, request
from werkzeug.exceptions import NotFound, InternalServerError, HTTPException
import logging

# local imports
from .model import Bookmarks, BookmarksApi


bookmarks = Blueprint("bookmarks", __name__, template_folder="templates")

# Loggers
log_user_activity = logging.getLogger("user")
# log_api_usage = logging.getLogger("api")
log_errors = logging.getLogger("errors")


@bookmarks.route("/")
def bookmarks_index():
    """ Bookmarks index view """

    log_user_activity.info(str(request))

    try:
        bookmarks_page = Bookmarks()

        return render_template("bookmarks.html", bookmarks_page=bookmarks_page)

    except (TypeError, KeyError, ValueError, OSError) as e:
        log_errors.error(str(e))
        raise InternalServerError

    except HTTPException as e:
        log_errors.error(str(e))
        raise e


@bookmarks.route("/<func>/<int:post_id>")
def bookmarks_handle(func, post_id):
    """ Bookmarks api view """

    log_user_activity.info(str(request))

    # for jump to post anchor
    anchor = ""

    try:
        bookmarks_api = BookmarksApi()

        if func == "add":
            if not bookmarks_api.check_post_id(post_id):
                raise NotFound()
            bookmarks_api.add(post_id)
            anchor = f"POST_ID_{post_id}"

        elif func == "remove":
            if not bookmarks_api.check_bookmark_id(post_id):
                raise NotFound()
            bookmarks_api.remove(post_id)

        else:
            raise NotFound()

        return redirect(url_for("feed.feed_index", _anchor=anchor), code=302)

    except (TypeError, KeyError, ValueError, OSError) as e:
        log_errors.error(str(e))
        raise InternalServerError()

    except HTTPException as e:
        log_errors.error(str(e))
        raise e
