"""
    Coursework №3
    Golosov_SA aka grm
    link: https://skyengpublic.notion.site/3-d2893a166cf0479a8c8bb3bfb13d478e#70281dd53e6e4930843e2501562a72f2

    Test data from feed blueprint
"""

# global imports
import os
import pytest
import json


# local imports
from ..data import RawPost, FullPost, ShortPost, PostHandler

dataclass_fields = pytest.mark.parametrize(
    "field, type_of",
    [
        ("poster_name", str),
        ("poster_avatar", str),
        ("pic", str),
        ("content", str),
        ("views_count", int),
        ("likes_count", int),
        ("pk", int)
    ]
)


@pytest.fixture
def test_post_record():
    return {
        "poster_name": "leo",
        "poster_avatar": "https://randus.org/avatars/w/c1819dbdffffff18.png",
        "pic": "https://images.unsplash.com/photo-1525351326368-efbb5cb6814d?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=580&q=80",
        "content": "Ага, опять еда! Квадратная #тарелка в квадратном кадре. А на тарелке, наверное, #пирог! Мне было так жаль, что я не могу ее съесть. Я боялась, что они заметят, и если я не съем это, то, значит, они все подумают, что я плохая девочка... Но потом мне вспомнилось, как они на меня смотрели. Когда я была маленькой, на кухне всегда были родители, бабушка, дедушка, дядя Борис... Все вместе. И всегда одна я, потому что все остальные приходили туда лишь изредка. Мне казалось, если бы все ходили на работу, как и я, в этот свой офис, было бы совсем неинтересно.",
        "views_count": 389,
        "likes_count": 157,
        "pk": 1
    }


@pytest.fixture
def test_data(test_app):
    folder = test_app.config["APP_DATA_FOLDER"]
    filename = test_app.config["APP_DATA_POSTS"]
    with open(os.path.join(folder, filename), "rt", encoding="utf-8") as fin:
        data = json.load(fin)
    return data


class TestFeedPosts:

    def test_raw_post_dataclass_init(self, test_post_record):
        try:
            raw_post = RawPost(**test_post_record)
        except Exception as e:
            assert False, f"There should be no exceptions. ({type(e)}: {e})"

    def test_full_post_dataclass_init(self, test_app, test_post_record):
        try:
            full_post = FullPost(**test_post_record)
        except Exception as e:
            assert False, f"There should be no exceptions. ({type(e)}: {e})"

    def test_short_post_dataclass_init(self, test_app, test_post_record):
        try:
            short_post = ShortPost(**test_post_record)
        except Exception as e:
            assert False, f"There should be no exceptions. ({type(e)}: {e})"

    @dataclass_fields
    def test_raw_post_fields(self, field, type_of, test_post_record):

        raw_post = RawPost(**test_post_record)

        assert hasattr(raw_post, field), f"Must have a field {field}"
        assert type(getattr(raw_post, field)) is type_of, f"Must have a type {type_of}"

    @dataclass_fields
    def test_full_post_fields(self, field, type_of, test_post_record):

        full_post = FullPost(**test_post_record)

        assert hasattr(full_post, field), f"Must have a field {field}"
        assert type(getattr(full_post, field)) is type_of, f"Must have a type {type_of}"

    @dataclass_fields
    def test_short_post_fields(self, field, type_of, test_post_record):

        full_post = ShortPost(**test_post_record)

        assert hasattr(full_post, field), f"Must have a field {field}"
        assert type(getattr(full_post, field)) is type_of, f"Must have a type {type_of}"

    def test_post_handler_raw_post(self, test_app):

        try:
            post_handler = PostHandler(RawPost)

        except Exception as e:
            assert False, f"There should be no exceptions. ({type(e)}: {e})"

    def test_post_handler_full_post(self, test_app):

        try:
            post_handler = PostHandler(FullPost)

        except Exception as e:
            assert False, f"There should be no exceptions. ({type(e)}: {e})"

    def test_post_handler_short_post(self, test_app):

        try:
            post_handler = PostHandler(ShortPost)

        except Exception as e:
            assert False, f"There should be no exceptions. ({type(e)}: {e})"

    def test_post_handler_select_all_raw_post(self, test_app, test_data):

        post_handler = PostHandler(RawPost)

        raw_data = post_handler.select_all()

        assert type(raw_data) is list, "Must be a list"
        assert len(raw_data) == len(test_data), "Must be equal"
        assert type(raw_data[0]) is RawPost, "Nust be a RawPost"

    def test_post_handler_select_all_full_post(self, test_app, test_data):

        post_handler = PostHandler(FullPost)

        full_data = post_handler.select_all()

        assert type(full_data) is list, "Must be a list"
        assert len(full_data) == len(test_data), "Must be equal"
        assert type(full_data[0]) is FullPost, "Nust be a RawPost"

    def test_post_handler_select_all_short_post(self, test_app, test_data):

        post_handler = PostHandler(ShortPost)

        short_data = post_handler.select_all()

        assert type(short_data) is list, "Must be a list"
        assert len(short_data) == len(test_data), "Must be equal"
        assert type(short_data[0]) is ShortPost, "Nust be a RawPost"

    @pytest.mark.parametrize("dataclass_post", [RawPost, FullPost, ShortPost])
    @pytest.mark.parametrize("post_id", [1, 2, 3, 4, 5, 6, 7, 8])
    @dataclass_fields
    def test_post_handler_select_by_id(self, dataclass_post, post_id, field, type_of, test_app, test_data):

        handler = PostHandler(dataclass_post)
        post_by_id = handler.select_one_by_pk(post_id)
        assert type(getattr(post_by_id, field)) is type_of, f"Must be {type_of}"
        if field != "content":
            assert getattr(post_by_id, field) == test_data[post_id - 1][field], "Must be equal"

    @pytest.mark.parametrize("dataclass_post", [FullPost, ShortPost])
    def test_dataclass_post_hashtag_replacement(self, dataclass_post, test_app, test_post_record):

        dataclass_post = dataclass_post(**test_post_record)

        assert "<a" in dataclass_post.content, "Must be replaced with '<a'"

    @pytest.mark.parametrize("dataclass_post", [RawPost, FullPost, ShortPost])
    @pytest.mark.parametrize("post_id", list(range(1, 9)))
    def test_increment_views_count_by_pk(self, dataclass_post, post_id, test_app):

        handler = PostHandler(dataclass_post)

        old_value = handler.select_one_by_pk(post_id).views_count

        handler.increment_views_count_by_pk(post_id)

        value = handler.select_one_by_pk(post_id).views_count

        assert value == old_value + 1, "Must be greater by 1"

    @pytest.mark.parametrize("dataclass_post", [RawPost, FullPost, ShortPost])
    @pytest.mark.parametrize("post_id", list(range(1, 9)))
    def test_increment_likes_count_by_pk(self, dataclass_post, post_id, test_app):

        handler = PostHandler(dataclass_post)

        old_value = handler.select_one_by_pk(post_id).likes_count

        handler.increment_likes_count_by_pk(post_id)

        value = handler.select_one_by_pk(post_id).likes_count

        assert value == old_value + 1, "Must be greater by 1"

    @pytest.mark.parametrize("dataclass_post", [RawPost, FullPost, ShortPost])
    def test_get_posts_count(self, dataclass_post, test_app):

        handler = PostHandler(dataclass_post)

        posts_count = handler.get_posts_count()

        assert posts_count == 8, "Must be 8"

    @pytest.mark.parametrize("dataclass_post", [RawPost, FullPost, ShortPost])
    @pytest.mark.parametrize("substring, count", [
        ("кот", 4),
        ("кОт", 4),
        ("  кот", 4),
        ("КОТ  ", 4),
        ("non-exist", 0),
        ("очень", 3),
        (",", 8)
    ])
    def test_select_by_substring(self, dataclass_post, substring, count, test_app):

        handler = PostHandler(dataclass_post)

        posts_count = len(handler.select_by_substring(substring))

        assert posts_count == count, "Must be equal"

    @pytest.mark.parametrize("dataclass_post", [RawPost, FullPost, ShortPost])
    @pytest.mark.parametrize("username, count", [
        ("leo", 2),
        ("johnny", 2),
        ("  hank", 2),
        ("larry  ", 2),
        ("joHNny", 2),
        ("JOHNNY", 2),
        ("non-exist", 0)
    ])
    def test_select_by_username(self, dataclass_post, username, count, test_app):

        handler = PostHandler(dataclass_post)

        posts_count = len(handler.select_by_username(username))

        assert posts_count == count, "Must be equal"

    @pytest.mark.parametrize("dataclass_post", [RawPost, FullPost, ShortPost])
    @pytest.mark.parametrize("substring, count", [
        ("кот", 4),
        ("кОт", 4),
        ("  кот", 4),
        ("КОТ  ", 4),
        ("non-exist", 0),
        ("очень", 3),
        (",", 8)
    ])
    def get_posts_count_by_substring(self, dataclass_post, substring, count, test_app):

        handler = PostHandler(dataclass_post)

        posts_count = len(handler.get_posts_count_by_substring(substring))

        assert posts_count == count, "Must be equal"
