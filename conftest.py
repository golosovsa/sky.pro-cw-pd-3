"""
    Coursework №3
    Golosov_SA aka grm
    link: https://skyengpublic.notion.site/3-d2893a166cf0479a8c8bb3bfb13d478e#70281dd53e6e4930843e2501562a72f2

    App file
"""


import pytest
from flask import Flask

from app import create_app
from config.testing import TestingConfig


@pytest.fixture(scope="module")
def test_app():
    """ Fixture for testing the app """

    app: Flask = create_app()
    app.config.from_object(TestingConfig)

    with app.app_context(), app.test_request_context():
        yield app
