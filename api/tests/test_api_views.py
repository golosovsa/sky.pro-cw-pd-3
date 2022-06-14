"""
    Coursework №3
    Golosov_SA aka grm
    link: https://skyengpublic.notion.site/3-d2893a166cf0479a8c8bb3bfb13d478e#70281dd53e6e4930843e2501562a72f2

    Test views from api blueprint
"""

# global imports
import pytest


class TestApiViews:

    def test_api_usage_view(self, test_app):

        resp: "TestResponse" = test_app.test_client().get(f"/api/")

        assert b"USAGE" in resp.data, "Must have substring 'USAGE'"
        assert resp.status_code == 200, "Must be 200"

    @pytest.mark.parametrize("method", ["post", "delete", "put"])
    def test_api_usage_view_wrong_method(self, method, test_app):
        test_method = getattr(test_app.test_client(), method)

        resp: "TestResponse" = test_method("/api/")

        assert resp.status_code == 405, "Must be 405"

    @pytest.mark.parametrize("post_id", list(range(1, 9)))
    def test_api_post(self, post_id, test_app):

        resp: "TestResponse" = test_app.test_client().get(f"/api/posts/{post_id}")

        assert resp.status_code == 200, "Must be 200"
        assert resp.mimetype == "application/json", "Must be 'application/json'"

    @pytest.mark.parametrize("post_id", [0, 99])
    def test_api_post_wrong_parameters(self, post_id, test_app):

        resp: "TestResponse" = test_app.test_client().get(f"/api/posts/{post_id}")

        assert resp.status_code == 200, "Must be 200"
        assert resp.mimetype == "application/json", "Must be 'application/json'"
        assert b"null" in resp.data, "Must have substring 'null'"

    def test_api_post_all(self, test_app):

        resp: "TestResponse" = test_app.test_client().get(f"/api/posts")

        assert resp.status_code == 200, "Must be 200"
        assert resp.mimetype == "application/json", "Must be 'application/json'"

