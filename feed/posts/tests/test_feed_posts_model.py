"""
    Coursework №3
    Golosov_SA aka grm
    link: https://skyengpublic.notion.site/3-d2893a166cf0479a8c8bb3bfb13d478e#70281dd53e6e4930843e2501562a72f2

    Test model from feed.posts blueprint
"""


# global imports
import pytest


# local imports
from feed.posts.model import Post
from feed.data import FullPost, PostHandler
from ..data import Comment
from feed.bookmarks.data import Bookmark, BookmarkHandler


class TestPostsModel:

    @pytest.mark.parametrize("post_id", list(range(1, 9)))
    def test_posts_model(self, post_id, test_app):

        bookmark_handler = BookmarkHandler(Bookmark)
        bookmark_handler.insert(1)
        post_page = Post(post_id)

        assert hasattr(post_page, "post"), "Must have a post"
        assert hasattr(post_page, "is_bookmarked"), "Must have a bookmarks"
        assert hasattr(post_page, "the_word_comments"), "Must have a count_posts"
        assert hasattr(post_page, "comments"), "Must have a comments"

        assert type(post_page.post) is FullPost, "Must be a FullPost"
        assert type(post_page.is_bookmarked) is bool, "Must be a bool"
        assert type(post_page.the_word_comments) is str, "Must be a str"
        assert type(post_page.comments) is list, "Must be a list"
        if post_page.comments:
            assert type(post_page.comments[0]) is Comment, "Must be a Comment"

    @pytest.mark.parametrize("post_id", [-1, 0, 99, "1", None])
    def test_posts_model_wrong_params(self, post_id, test_app):

        bookmark_handler = BookmarkHandler(Bookmark)
        bookmark_handler.insert(1)
        post_page = Post(post_id)

        assert hasattr(post_page, "post"), "Must have a post"
        assert hasattr(post_page, "is_bookmarked"), "Must have a bookmarks"
        assert hasattr(post_page, "the_word_comments"), "Must have a count_posts"
        assert hasattr(post_page, "comments"), "Must have a comments"

        assert post_page.post is None, "Must be a None"
        assert type(post_page.is_bookmarked) is bool, "Must be a bool"
        assert type(post_page.the_word_comments) is str, "Must be a str"
        assert type(post_page.comments) is list, "Must be a list"
        assert len(post_page.comments) == 0, "Must be 0"

    @pytest.mark.parametrize("post_id", list(range(1, 9)))
    def test_search_model_increment_views(self, post_id, test_app):
        post_handler = PostHandler(FullPost)
        old_value = post_handler.select_one_by_pk(post_id).views_count

        post_page = Post(post_id)

        new_value = post_handler.select_one_by_pk(post_id).views_count

        assert new_value == old_value + 1, "Must be greater that by 1"


