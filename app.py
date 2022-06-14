"""
    Coursework №3
    Golosov_SA aka grm
    link: https://skyengpublic.notion.site/3-d2893a166cf0479a8c8bb3bfb13d478e#70281dd53e6e4930843e2501562a72f2

    App file
"""

# global imports
import dotenv
import os
from flask import Flask
from werkzeug.exceptions import InternalServerError, HTTPException

# local imports
from api.views import api
from config import DevelopmentConfig, ProductionConfig
from feed.views import feed
from loggers import init_loggers


def create_app():
    """ Create the the_app """

    # place APP_CONFIG="production" in file .env before deploy
    dotenv.load_dotenv(override=True)
    the_app = Flask(__name__, static_folder="static", template_folder="templates")

    # the_app config
    app_config = os.environ.get("APP_CONFIG", None)
    if app_config == "development":
        the_app.config.from_object(DevelopmentConfig)
    elif app_config == "production":
        the_app.config.from_object(ProductionConfig)
    else:
        raise InternalServerError("The APP_CONFIG application environment variable does not exist.\n"
                                  "Make sure that the .env file is correct or exists.")

    # loggers
    init_loggers(the_app)

    # global blueprints
    the_app.register_blueprint(feed, url_prefix="/")
    the_app.register_blueprint(api, url_prefix="/api/")

    @the_app.errorhandler(HTTPException)
    def app_handle_errors(e: HTTPException):
        return f"<h1>ERROR</h1><p>{e.description}</p>", e.code

    return the_app


app = create_app()


# main app enter point here
if __name__ == '__main__':
    app.run()
