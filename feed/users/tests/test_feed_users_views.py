"""
    Coursework №3
    Golosov_SA aka grm
    link: https://skyengpublic.notion.site/3-d2893a166cf0479a8c8bb3bfb13d478e#70281dd53e6e4930843e2501562a72f2

    Test views from feed.users blueprint
"""


# global imports
import pytest


class TestUsersView:

    @pytest.mark.parametrize("username", ["leo", "johnny", "hank", "larry", "  leo", "johnny  ", "HaNk", "LARRY"])
    def test_users_view(self, username, test_app):

        resp: "TestResponse" = test_app.test_client().get(f"/users/{username}")

        assert resp.status_code == 200, "Must be 200"

    @pytest.mark.parametrize("username", ["вася", "саша", "петя", "оля", "маша", "таня", "вова", "витя"])
    def test_users_view_wrong_param(self, username, test_app):

        resp: "TestResponse" = test_app.test_client().get(f"/users/{username}")

        assert resp.status_code == 404, "Must be 404"

    @pytest.mark.parametrize("method", ["post", "delete", "put"])
    def test_users_view_wrong_method(self, method, test_app):

        test_method = getattr(test_app.test_client(), method)

        resp: "TestResponse" = test_method("/users/leo")

        assert resp.status_code == 405, "Must be 405"

