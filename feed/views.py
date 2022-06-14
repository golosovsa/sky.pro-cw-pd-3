"""
    Coursework №3
    Golosov_SA aka grm
    link: https://skyengpublic.notion.site/3-d2893a166cf0479a8c8bb3bfb13d478e#70281dd53e6e4930843e2501562a72f2

    Views from feed blueprint
"""

# global imports
from flask import Blueprint, render_template, request
from werkzeug.exceptions import InternalServerError, HTTPException
import logging

# local blueprints imports (alphabetic order ;)
from .bookmarks.views import bookmarks
from .likes.views import likes
from .posts.views import posts
from .search.views import search
from .tag.views import tag
from .users.views import users

# local model import
from .model import Feed

# the feed blueprint
feed = Blueprint("feed", __name__, template_folder="templates")

# local blueprints registration and prefix definition
feed.register_blueprint(posts, url_prefix="/posts/")
feed.register_blueprint(search, url_prefix="/search/")
feed.register_blueprint(users, url_prefix="/users/")
feed.register_blueprint(tag, url_prefix="/tag/")
feed.register_blueprint(bookmarks, url_prefix="/bookmarks/")
feed.register_blueprint(likes, url_prefix="/likes/")


# Loggers
log_user_activity = logging.getLogger("user")
# log_api_usage = logging.getLogger("api")
log_errors = logging.getLogger("errors")


@feed.route("/")
def feed_index():
    """ Feed index view """

    log_user_activity.info(str(request))

    try:
        feed_page = Feed()

        return render_template("index.html", feed_page=feed_page)

    except (TypeError, ValueError, KeyError, OSError) as e:
        log_errors.error(str(e))
        raise InternalServerError()

    except HTTPException as e:
        log_errors.error(str(e))
        raise e

