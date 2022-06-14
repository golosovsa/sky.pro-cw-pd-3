"""
    Coursework №3
    Golosov_SA aka grm
    link: https://skyengpublic.notion.site/3-d2893a166cf0479a8c8bb3bfb13d478e#70281dd53e6e4930843e2501562a72f2

    Test model from feed blueprint
"""


# global imports
import pytest


# local imports
from ..model import Feed
from ..data import ShortPost
from ..bookmarks.data import Bookmark, BookmarkHandler


class TestFeedModel:

    def test_feed_model(self, test_app):

        bookmark_handler = BookmarkHandler(Bookmark)
        bookmark_handler.insert(1)
        feed_page = Feed()

        assert hasattr(feed_page, "posts"), "Must have a posts"
        assert hasattr(feed_page, "bookmarks"), "Must have a bookmarks"
        assert hasattr(feed_page, "is_post_in_bookmarks"), "Must have a is_post_in_bookmarks"

        test_value = feed_page.is_post_in_bookmarks(1)

        assert type(feed_page.posts) is list, "Must be a list"
        assert type(feed_page.posts[0]) is ShortPost, "Must be a ShortPost"
        assert type(feed_page.bookmarks) is list, "Must be a list"

        assert type(feed_page.bookmarks[0]) is Bookmark, "Must be a Bookmark"
        assert type(test_value) is bool, "Must be a bool"
