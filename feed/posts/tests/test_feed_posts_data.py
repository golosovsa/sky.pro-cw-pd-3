"""
    Coursework №3
    Golosov_SA aka grm
    link: https://skyengpublic.notion.site/3-d2893a166cf0479a8c8bb3bfb13d478e#70281dd53e6e4930843e2501562a72f2

    Test data from feed.posts blueprint
"""

# global imports
import os
import pytest
import json


# local imports
from ..data import Comment, CommentHandler


comment_dataclass_fields = pytest.mark.parametrize(
    "field, type_of",
    [
        ("post_id", int),
        ("commenter_name", str),
        ("comment", str),
        ("pk", int)
    ]
)


@pytest.fixture
def test_comments_record():
    return {
        "post_id": 1,
        "commenter_name": "hanna",
        "comment": "Очень здорово!",
        "pk": 1
    }


@pytest.fixture
def test_data(test_app):
    folder = test_app.config["APP_DATA_FOLDER"]
    filename = test_app.config["APP_DATA_COMMENTS"]
    with open(os.path.join(folder, filename), "rt", encoding="utf-8") as fin:
        data = json.load(fin)
    return data


class TestComments:

    def test_comment_dataclass_init(self, test_comments_record):
        try:
            raw_post = Comment(**test_comments_record)
        except Exception as e:
            assert False, f"There should be no exceptions. ({type(e)}: {e})"

    @comment_dataclass_fields
    def test_comments_fields(self, field, type_of, test_comments_record):

        raw_post = Comment(**test_comments_record)

        assert hasattr(raw_post, field), f"Must have a field {field}"
        assert type(getattr(raw_post, field)) is type_of, f"Must have a type {type_of}"

    def test_comments_handler_comment(self, test_app):

        try:
            post_handler = CommentHandler(Comment)

        except Exception as e:
            assert False, f"There should be no exceptions. ({type(e)}: {e})"

    @pytest.mark.parametrize("post_id", list(range(1, 9)))
    def test_comment_handler_select_all_comment(self, post_id, test_app, test_data):

        post_handler = CommentHandler(Comment)

        try:
            data = post_handler.select_by_post_id(post_id)

        except Exception as e:
            assert False, f"There should be no exceptions. ({type(e)}: {e})"

        assert type(data) is list, "Must be a list"
        if data:
            assert type(data[0]) is Comment, "Must be a Comment"

    @pytest.mark.parametrize("comment_id", list(range(1, 21)))
    @comment_dataclass_fields
    def test_post_handler_select_by_id(self, comment_id, field, type_of, test_app, test_data):

        handler = CommentHandler(Comment)
        post_by_id = handler.select_by_pk(comment_id)
        assert type(getattr(post_by_id, field)) is type_of, f"Must be {type_of}"
        assert getattr(post_by_id, field) == test_data[comment_id - 1][field], "Must be equal"

