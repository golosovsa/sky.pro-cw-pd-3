"""
    Coursework №3
    Golosov_SA aka grm
    link: https://skyengpublic.notion.site/3-d2893a166cf0479a8c8bb3bfb13d478e#70281dd53e6e4930843e2501562a72f2

    Test model from feed.search blueprint
"""


# global imports
import pytest


# local imports
from feed.search.model import Search
from feed.data import ShortPost
from feed.bookmarks.data import Bookmark, BookmarkHandler


class TestSearchModel:

    @pytest.mark.parametrize("substring", ["кОт", "  кот", "КОТ  ", "очень", ",", "КОТ  "])
    def test_search_model(self, substring, test_app):

        bookmark_handler = BookmarkHandler(Bookmark)
        bookmark_handler.insert(1)
        search_page = Search(substring)

        assert hasattr(search_page, "posts"), "Must have a posts"
        assert hasattr(search_page, "bookmarks"), "Must have a bookmarks"
        assert hasattr(search_page, "is_post_in_bookmarks"), "Must have a is_post_in_bookmarks"
        assert hasattr(search_page, "count_posts"), "Must have a count_posts"
        assert hasattr(search_page, "value"), "Must have a value"

        test_value = search_page.is_post_in_bookmarks(1)

        assert type(search_page.posts) is list, "Must be a list"
        assert type(search_page.posts[0]) is ShortPost, "Must be a ShortPost"
        assert type(search_page.bookmarks) is list, "Must be a list"
        assert type(search_page.count_posts) is str, "Must be a str"
        assert type(search_page.value) is str, "Must be a str"

        assert type(search_page.bookmarks[0]) is Bookmark, "Must be a Bookmark"
        assert type(test_value) is bool, "Must be a bool"

    @pytest.mark.parametrize("substring", ["", "\n", "\t"])
    def test_search_model_wrong_params(self, substring, test_app):

        bookmark_handler = BookmarkHandler(Bookmark)
        bookmark_handler.insert(1)
        search_page = Search(substring)

        assert hasattr(search_page, "posts"), "Must have a posts"
        assert hasattr(search_page, "bookmarks"), "Must have a bookmarks"
        assert hasattr(search_page, "is_post_in_bookmarks"), "Must have a is_post_in_bookmarks"
        assert hasattr(search_page, "count_posts"), "Must have a count_posts"
        assert hasattr(search_page, "value"), "Must have a value"

        test_value = search_page.is_post_in_bookmarks(1)

        assert type(search_page.posts) is list, "Must be a list"
        assert type(search_page.bookmarks) is list, "Must be a list"
        assert type(test_value) is bool, "Must be a bool"
        assert type(search_page.count_posts) is str, "Must be a str"
        assert type(search_page.value) is str, "Must be a str"

        assert len(search_page.posts) == 8, "Must be 8"
        assert len(search_page.bookmarks) != 0, "Must be not empty"

    @pytest.mark.parametrize("substring", ["non-exists", "[[[]]]", "<><><><!!>"])
    def test_search_model_non_exists(self, substring, test_app):
        bookmark_handler = BookmarkHandler(Bookmark)
        bookmark_handler.insert(1)
        search_page = Search(substring)

        assert hasattr(search_page, "posts"), "Must have a posts"
        assert hasattr(search_page, "bookmarks"), "Must have a bookmarks"
        assert hasattr(search_page, "is_post_in_bookmarks"), "Must have a is_post_in_bookmarks"
        assert hasattr(search_page, "count_posts"), "Must have a count_posts"
        assert hasattr(search_page, "value"), "Must have a value"

        test_value = search_page.is_post_in_bookmarks(1)

        assert type(search_page.posts) is list, "Must be a list"
        assert type(search_page.bookmarks) is list, "Must be a list"
        assert type(test_value) is bool, "Must be a bool"
        assert type(search_page.count_posts) is str, "Must be a str"
        assert type(search_page.value) is str, "Must be a str"

        assert len(search_page.posts) == 0, "Must be 0"
        assert len(search_page.bookmarks) != 0, "Must be not empty"
