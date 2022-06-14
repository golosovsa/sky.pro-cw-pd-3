"""
    Coursework №3
    Golosov_SA aka grm
    link: https://skyengpublic.notion.site/3-d2893a166cf0479a8c8bb3bfb13d478e#70281dd53e6e4930843e2501562a72f2

    Test model from feed.tag blueprint
"""


# global imports
import pytest


# local imports
from feed.tag.model import Tag
from feed.data import ShortPost
from feed.bookmarks.data import Bookmark, BookmarkHandler


class TestTagModel:

    @pytest.mark.parametrize("tag", ["кот", "котики", "инста", "инстаграм", "любовькживотным", "любимыйкот"])
    def test_tag_model(self, tag, test_app):

        bookmark_handler = BookmarkHandler(Bookmark)
        bookmark_handler.insert(1)
        tag_page = Tag(tag)

        assert hasattr(tag_page, "posts"), "Must have a posts"
        assert hasattr(tag_page, "bookmarks"), "Must have a bookmarks"
        assert hasattr(tag_page, "is_post_in_bookmarks"), "Must have a is_post_in_bookmarks"

        test_value = tag_page.is_post_in_bookmarks(1)

        assert type(tag_page.posts) is list, "Must be a list"
        assert type(tag_page.posts[0]) is ShortPost, "Must be a ShortPost"
        assert type(tag_page.bookmarks) is list, "Must be a list"

        assert type(tag_page.bookmarks[0]) is Bookmark, "Must be a Bookmark"
        assert type(test_value) is bool, "Must be a bool"

    @pytest.mark.parametrize("tag", ["#", "non-exists", "", " ", "\t", "\n"])
    def test_tag_model_wrong_tag(self, tag, test_app):

        bookmark_handler = BookmarkHandler(Bookmark)
        bookmark_handler.insert(1)
        tag_page = Tag(tag)

        assert hasattr(tag_page, "posts"), "Must have a posts"
        assert hasattr(tag_page, "bookmarks"), "Must have a bookmarks"
        assert hasattr(tag_page, "is_post_in_bookmarks"), "Must have a is_post_in_bookmarks"

        test_value = tag_page.is_post_in_bookmarks(1)

        assert type(tag_page.posts) is list, "Must be a list"
        assert type(tag_page.bookmarks) is list, "Must be a list"
        assert type(test_value) is bool, "Must be a bool"

        assert len(tag_page.posts) == 0, "Must be empty"
        assert len(tag_page.bookmarks) == 0, "Must be empty"
