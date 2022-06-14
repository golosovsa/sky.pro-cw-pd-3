"""
    Coursework №3
    Golosov_SA aka grm
    link: https://skyengpublic.notion.site/3-d2893a166cf0479a8c8bb3bfb13d478e#70281dd53e6e4930843e2501562a72f2

    Testing config class
"""


from .base import BaseConfig


class TestingConfig(BaseConfig):
    """ Testing config for internal flask wsgi server """

    TESTING = True

    APP_DATA_FOLDER = "./tests/data"
