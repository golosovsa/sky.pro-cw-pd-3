"""
    Coursework №3
    Golosov_SA aka grm
    link: https://skyengpublic.notion.site/3-d2893a166cf0479a8c8bb3bfb13d478e#70281dd53e6e4930843e2501562a72f2

    Test views from app
"""


# global imports
import pytest


class TestAppView:

    def test_app_handle_error(self, test_app):

        resp: "TestResponse" = test_app.test_client().get("/meow")

        assert resp.status_code == 404, "Must be 404"
        assert b"ERROR" in resp.data, "Must have include 'ERROR'"
