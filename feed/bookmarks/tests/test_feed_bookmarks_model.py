"""
    Coursework №3
    Golosov_SA aka grm
    link: https://skyengpublic.notion.site/3-d2893a166cf0479a8c8bb3bfb13d478e#70281dd53e6e4930843e2501562a72f2

    Test model from feed.bookmarks blueprint
"""


# global imports
import pytest


from ..model import Bookmarks, BookmarksApi
from ..data import BookmarkHandler, Bookmark
from feed.data import RawPost, ShortPost, PostHandler


class TestBookmarks:

    @pytest.mark.parametrize("post_id", list(range(1, 9)))
    def test_bookmarks_model(self, post_id, test_app):

        bookmarks_handle = BookmarkHandler(Bookmark)
        bookmarks_handle.flush()
        bookmarks_handle.insert(post_id)

        bookmarks_model = Bookmarks()

        assert hasattr(bookmarks_model, "data"), "Must have a data"
        assert type(bookmarks_model.data) is list, "Must be a list"
        assert type(bookmarks_model.data[0]) is dict, "Must be a dict"
        assert "post" in bookmarks_model.data[0], "Must have a post"
        assert "bookmark" in bookmarks_model.data[0], "Must have a post"
        assert type(bookmarks_model.data[0]["post"]) is ShortPost, "Must be a ShortPost"
        assert type(bookmarks_model.data[0]["bookmark"]) is Bookmark, "Must be a Bookmark"

    @pytest.mark.parametrize("post_id", [-1, 0, 99, "non-exists"])
    def test_bookmarks_model_wrong_parameter(self, post_id, test_app):

        bookmarks_handle = BookmarkHandler(Bookmark)
        bookmarks_handle.flush()
        bookmarks_handle.insert(post_id)

        bookmarks_model = Bookmarks()

        assert hasattr(bookmarks_model, "data"), "Must have a data"
        assert type(bookmarks_model.data) is list, "Must be a list"
        assert len(bookmarks_model.data) == 0, "Must be empty"

    def test_bookmarks_api_model(self, test_app):

        bookmarks_api = BookmarksApi()

        assert hasattr(bookmarks_api, "bookmark_handler"), "Must have a bookmark_handler"
        assert hasattr(bookmarks_api, "post_handler"), "Must have a post_handler"
        assert hasattr(bookmarks_api, "add"), "Must have a add"
        assert hasattr(bookmarks_api, "remove"), "Must have a remove"
        assert hasattr(bookmarks_api, "check_post_id"), "Must have a check_post_id"
        assert hasattr(bookmarks_api, "check_bookmark_id"), "Must have a check_bookmark_id"

        assert type(bookmarks_api.bookmark_handler) is BookmarkHandler, "Must be a BookmarkHandler"
        assert type(bookmarks_api.post_handler) is PostHandler, "Must be a PostHandler"
        assert bookmarks_api.post_handler.DataClass is RawPost, "Must be a ShortPost"



