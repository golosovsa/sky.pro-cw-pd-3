"""
    Coursework №3
    Golosov_SA aka grm
    link: https://skyengpublic.notion.site/3-d2893a166cf0479a8c8bb3bfb13d478e#70281dd53e6e4930843e2501562a72f2

    Development config class
"""


from .base import BaseConfig


class DevelopmentConfig(BaseConfig):
    """ Development config for internal flask wsgi server """
    APP_DATA_FOLDER = "./data"
