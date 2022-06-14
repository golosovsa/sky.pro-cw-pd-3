"""
    Coursework №3
    Golosov_SA aka grm
    link: https://skyengpublic.notion.site/3-d2893a166cf0479a8c8bb3bfb13d478e#70281dd53e6e4930843e2501562a72f2

    Test views from feed.bookmarks blueprint
"""

# global imports
import pytest


# local imports
from ..data import BookmarkHandler, Bookmark


class TestBookmarksViews:

    def test_bookmarks_view(self, test_app):

        resp: "TestResponse" = test_app.test_client().get(f"/bookmarks/")

        assert resp.status_code == 200, "Must be 200"

    @pytest.mark.parametrize("post_id", list(range(1, 9)))
    def test_bookmarks_add_api_view(self, post_id, test_app):
        handler = BookmarkHandler(Bookmark)
        handler.flush()

        resp: "TestResponse" = test_app.test_client().get(f"/bookmarks/add/{post_id}")

        assert resp.status_code == 302, "Must be 302"

    @pytest.mark.parametrize("post_id", list(range(1, 9)))
    def test_bookmarks_remove_api_view(self, post_id, test_app):
        handler = BookmarkHandler(Bookmark)
        handler.flush()
        handler.insert(post_id)

        resp: "TestResponse" = test_app.test_client().get(f"/bookmarks/remove/0")

        assert resp.status_code == 302, "Must be 302"

    @pytest.mark.parametrize("function", ["non-exists", 1, "addremove", "ADD", "ReMove"])
    def test_bookmarks_add_api_view(self, function, test_app):
        handler = BookmarkHandler(Bookmark)
        handler.flush()

        resp: "TestResponse" = test_app.test_client().get(f"/bookmarks/{function}/1")

        assert resp.status_code == 404, "Must be 404"

    @pytest.mark.parametrize("method", ["post", "delete", "put"])
    def test_bookmarks_view_wrong_method(self, method, test_app):

        test_method = getattr(test_app.test_client(), method)

        resp: "TestResponse" = test_method("/bookmarks/")

        assert resp.status_code == 405, "Must be 405"

    @pytest.mark.parametrize("method", ["post", "delete", "put"])
    def test_bookmarks_api_view_wrong_method(self, method, test_app):
        test_method = getattr(test_app.test_client(), method)

        resp: "TestResponse" = test_method("/bookmarks/add/1")

        assert resp.status_code == 405, "Must be 405"
