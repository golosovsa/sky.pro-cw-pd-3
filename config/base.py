"""
    Coursework №3
    Golosov_SA aka grm
    link: https://skyengpublic.notion.site/3-d2893a166cf0479a8c8bb3bfb13d478e#70281dd53e6e4930843e2501562a72f2

    Base config class
"""


class BaseConfig:
    """ Base app config class """

    # app data config
    APP_DATA_FOLDER = ""
    APP_DATA_POSTS = "posts.json"
    APP_DATA_COMMENTS = "comments.json"
    APP_DATA_BOOKMARKS = "bookmarks.json"

    # OS io config
    IO_ATTEMPTS = 10
    IO_SLEEP_FOR = 0.2

    # App blueprints config
    SEARCH_DEPTH = 10

    # flask config
    JSON_AS_ASCII = False

    # logging config
    APP_LOG_DIR = "logs/"
    APP_LOG_EXCEPTION_ERRORS_FILE = "errors.log"
    APP_LOG_API_USAGE_FILE = "api.log"
    APP_LOG_USER_ACTIVITY_FILE = "user.log"
