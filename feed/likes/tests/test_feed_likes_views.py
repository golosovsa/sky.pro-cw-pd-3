"""
    Coursework №3
    Golosov_SA aka grm
    link: https://skyengpublic.notion.site/3-d2893a166cf0479a8c8bb3bfb13d478e#70281dd53e6e4930843e2501562a72f2

    Test views from feed.likes blueprint
"""

# global imports
import pytest


class TestLikesView:

    @pytest.mark.parametrize("post_id", list(range(1, 9)))
    def test_likes_view(self, post_id, test_app):

        resp: "TestResponse" = test_app.test_client().get(f"/likes/add/{post_id}")

        assert resp.status_code == 302, "Must be 302"

    @pytest.mark.parametrize("post_id", [-1, 0, 99, None, "non-exists"])
    def test_likes_view_wrong_param(self, post_id, test_app):

        resp: "TestResponse" = test_app.test_client().get(f"/likes/add/{post_id}")

        assert resp.status_code == 404, "Must be 404"

    @pytest.mark.parametrize("method", ["post", "delete", "put"])
    def test_likes_view_wrong_method(self, method, test_app):

        test_method = getattr(test_app.test_client(), method)

        resp: "TestResponse" = test_method("/likes/add/1")

        assert resp.status_code == 405, "Must be 405"
