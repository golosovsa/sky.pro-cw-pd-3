"""
    Coursework №3
    Golosov_SA aka grm
    link: https://skyengpublic.notion.site/3-d2893a166cf0479a8c8bb3bfb13d478e#70281dd53e6e4930843e2501562a72f2

    Test model from api blueprint
"""


# global imports
import pytest

# local imports
from feed.data import RawPost, PostHandler
from ..model import ApiPost


class TestApiModel:

    def test_api_post_model(self, test_app):

        api_post = ApiPost()

        assert hasattr(api_post, "post_handler"), "Must have a post_handler"
        assert hasattr(api_post, "get_all"), "Must have a get_all"
        assert hasattr(api_post, "get_one"), "Must have a get_one"

        assert type(api_post.post_handler) is PostHandler, "Must be a PostHandler"
        assert api_post.post_handler.DataClass is RawPost, "Must be a RawPost"
