"""
    Coursework №3
    Golosov_SA aka grm
    link: https://skyengpublic.notion.site/3-d2893a166cf0479a8c8bb3bfb13d478e#70281dd53e6e4930843e2501562a72f2

    Test data from feed.bookmarks blueprint
"""

# global imports
import os
import pytest
import json


# local imports
from ..data import Bookmark, BookmarkHandler
from grm import DAO


dataclass_bookmark_fields = pytest.mark.parametrize(
    "field, type_of",
    [
        ("post_id", int),
        ("pk", int)
    ]
)


@pytest.fixture
def test_bookmark_record():
    return {
        "post_id": 1,
        "pk": 0
    }


@pytest.fixture
def test_data(test_app):
    folder = test_app.config["APP_DATA_FOLDER"]
    filename = test_app.config["APP_DATA_BOOKMARKS"]
    with open(os.path.join(folder, filename), "rt", encoding="utf-8") as fin:
        data = json.load(fin)
    return data


class TestBookmarks:

    def test_bookmark_dataclass_init(self, test_bookmark_record):
        try:
            the_bookmark = Bookmark(**test_bookmark_record)
        except Exception as e:
            assert False, f"There should be no exceptions. ({type(e)}: {e})"

    @dataclass_bookmark_fields
    def test_bookmark_fields(self, field, type_of, test_bookmark_record):

        the_bookmark = Bookmark(**test_bookmark_record)

        assert hasattr(the_bookmark, field), f"Must have a field {field}"
        assert type(getattr(the_bookmark, field)) is type_of, f"Must have a type {type_of}"

    def test_bookmark_handler_bookmark(self, test_app):

        try:
            bookmark_handler = BookmarkHandler(Bookmark)

        except Exception as e:
            assert False, f"There should be no exceptions. ({type(e)}: {e})"

    def test_bookmark_handler_select_all_bookmark(self, test_app, test_data):

        bookmark_handler = BookmarkHandler(Bookmark)
        bookmark_handler.flush()
        bookmark_handler.insert(1)

        bookmark_data = bookmark_handler.select_all()

        assert type(bookmark_data) is list, "Must be a list"
        assert len(bookmark_data) == len(bookmark_data), "Must be equal"
        assert type(bookmark_data[0]) is Bookmark, "Nust be a RawPost"

    @pytest.mark.parametrize("bookmark_id", [0, 1, 2, 3, 4, 5, 6, 7])
    @dataclass_bookmark_fields
    def test_bookmark_handler_select_by_id(self, bookmark_id, field, type_of, test_app, test_data):

        handler = BookmarkHandler(Bookmark)
        handler.flush()
        [handler.insert(i + 1) for i in range(8)]
        bookmark_by_id = handler.select_one_by_pk(bookmark_id)
        assert type(getattr(bookmark_by_id, field)) is type_of, f"Must be {type_of}"
        assert getattr(bookmark_by_id, field) == test_data[bookmark_id][field], "Must be equal"

    @pytest.mark.parametrize("post_id", [1, 2, 3, 4, 5, 6, 7, 8])
    @dataclass_bookmark_fields
    def test_bookmark_handler_select_by_post_id(self, post_id, field, type_of, test_app):

        handler = BookmarkHandler(Bookmark)
        [handler.delete(i) for i in range(8)]
        handler = BookmarkHandler(Bookmark)
        [handler.insert(i + 1) for i in range(8)]
        bookmark_by_id = handler.select_one_by_post_id(post_id)
        assert type(getattr(bookmark_by_id, field)) is type_of, f"Must be {type_of}"

    @pytest.mark.parametrize("post_id", [1, 2, 3, 4, 5, 6, 7, 8])
    def test_bookmark_handler_insert(self, post_id, test_app):

        handler = BookmarkHandler(Bookmark)
        handler.flush()

        try:
            handler.insert(post_id)
            handler.delete(handler.select_one_by_post_id(post_id).pk)

        except Exception as e:
            assert False, f"There should be no exceptions. ({type(e)}: {e})"

        assert len(handler.select_all()) == 0, "Must be empty"

