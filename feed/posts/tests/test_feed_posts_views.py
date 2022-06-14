"""
    Coursework №3
    Golosov_SA aka grm
    link: https://skyengpublic.notion.site/3-d2893a166cf0479a8c8bb3bfb13d478e#70281dd53e6e4930843e2501562a72f2

    Test views from feed.posts blueprint
"""

# global imports
import pytest


class TestSearchView:

    @pytest.mark.parametrize("post_id", list(range(1, 9)))
    def test_search_view(self, post_id, test_app):

        resp: "TestResponse" = test_app.test_client().get(f"/posts/{post_id}")

        assert resp.status_code == 200, "Must be 200"

    @pytest.mark.parametrize("post_id", [-1, 0, 99, None, "non-exists"])
    def test_search_view_wrong_param(self, post_id, test_app):

        resp: "TestResponse" = test_app.test_client().get(f"/posts/{post_id}")

        assert resp.status_code == 404, "Must be 404"

    @pytest.mark.parametrize("method", ["post", "delete", "put"])
    def test_search_view_wrong_method(self, method, test_app):

        test_method = getattr(test_app.test_client(), method)

        resp: "TestResponse" = test_method("/posts/1")

        assert resp.status_code == 405, "Must be 405"
