"""
    Coursework №3
    Golosov_SA aka grm
    link: https://skyengpublic.notion.site/3-d2893a166cf0479a8c8bb3bfb13d478e#70281dd53e6e4930843e2501562a72f2

    Test model from feed.users blueprint
"""


# global imports
import pytest


# local imports
from ..model import Users
from feed.data import ShortPost
from feed.bookmarks.data import Bookmark, BookmarkHandler


class TestUsersModel:

    @pytest.mark.parametrize("username, count", [
        ("leo", 2),
        ("johnny", 2),
        ("hank", 2),
        ("larry", 2),
        ("non-exist", 0)
    ])
    def test_feed_users(self, username, count, test_app):

        bookmark_handler = BookmarkHandler(Bookmark)
        bookmark_handler.insert(1)
        users_page = Users(username)

        assert hasattr(users_page, "posts"), "Must have a posts"
        assert hasattr(users_page, "bookmarks"), "Must have a bookmarks"
        assert hasattr(users_page, "is_post_in_bookmarks"), "Must have a is_post_in_bookmarks"

        assert len(users_page.posts) == count, f"Must be {count}"

        if count == 0:
            return

        test_value = users_page.is_post_in_bookmarks(1)

        assert type(users_page.posts) is list, "Must be a list"
        assert type(users_page.posts[0]) is ShortPost, "Must be a ShortPost"
        assert type(users_page.bookmarks) is list, "Must be a list"

        assert type(users_page.bookmarks[0]) is Bookmark, "Must be a Bookmark"
        assert type(test_value) is bool, "Must be a bool"
