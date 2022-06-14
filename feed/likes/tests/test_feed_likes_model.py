"""
    Coursework №3
    Golosov_SA aka grm
    link: https://skyengpublic.notion.site/3-d2893a166cf0479a8c8bb3bfb13d478e#70281dd53e6e4930843e2501562a72f2

    Test model from feed.likes blueprint
"""


# global imports
import pytest


# local imports
from feed.likes.model import LikesApi
from feed.data import RawPost, PostHandler


class TestPostsModel:

    @pytest.mark.parametrize("post_id", list(range(1, 9)))
    def test_likes_model(self, post_id, test_app):

        likes_api = LikesApi(post_id)

        assert hasattr(likes_api, "post"), "Must have a post"
        assert type(likes_api.post) is RawPost, "Must be a RawPost"

    @pytest.mark.parametrize("post_id", [-1, 0, 99, "1", None])
    def test_likes_model_wrong_params(self, post_id, test_app):
        likes_api = LikesApi(post_id)

        assert hasattr(likes_api, "post"), "Must have a post"
        assert likes_api.post is None, "Must be a None"

    @pytest.mark.parametrize("post_id", list(range(1, 9)))
    def test_likes_model_increment_likes(self, post_id, test_app):

        post_handler = PostHandler(RawPost)
        old_value = post_handler.select_one_by_pk(post_id).likes_count

        likes_api = LikesApi(post_id)

        new_value = post_handler.select_one_by_pk(post_id).likes_count

        assert new_value == old_value + 1, "Must be greater that by 1"
