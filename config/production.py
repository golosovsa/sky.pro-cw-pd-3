"""
    Coursework №3
    Golosov_SA aka grm
    link: https://skyengpublic.notion.site/3-d2893a166cf0479a8c8bb3bfb13d478e#70281dd53e6e4930843e2501562a72f2

    Production config class
"""


from .base import BaseConfig


class ProductionConfig(BaseConfig):
    """ Production config for deploying """
    APP_DATA_FOLDER = "/home/golosovsa/data"
