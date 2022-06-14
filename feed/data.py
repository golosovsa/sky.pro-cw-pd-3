"""
    Coursework №3
    Golosov_SA aka grm
    link: https://skyengpublic.notion.site/3-d2893a166cf0479a8c8bb3bfb13d478e#70281dd53e6e4930843e2501562a72f2

    Data from feed blueprint
"""

# global imports
import os
import re
from dataclasses import dataclass, field, asdict
from flask import current_app, url_for
from werkzeug.urls import url_unquote_plus

# local imports
from grm import DAO, Singleton


@dataclass(frozen=True, order=True)
class RawPost:
    """ Raw data class (repeat database record) """
    poster_name: str = field(compare=False)
    poster_avatar: str = field(compare=False)
    pic: str = field(compare=False)
    content: str = field(compare=False)
    views_count: int = field(compare=False)
    likes_count: int = field(compare=False)
    pk: int


@dataclass(frozen=True, order=True)
class FullPost(RawPost):
    """ Full post data class (hashtags are replaced with links) """
    def __post_init__(self):
        self.replace_hashtags()

    def replace_hashtags(self):
        """ Replace hashtags (helper method) """

        def replace(match: re.Match):
            """ replace function (for re compile) """
            tag_name = match.group("tag_name")
            url_tag = url_for("feed.tag.tag_index", tag_name=tag_name)
            url_tag = url_unquote_plus(url_tag, charset="utf-8", errors="strict")
            return f'<a class="hashtag" href="{url_tag}">#{tag_name}</a>'

        content = self.content
        re_pattern = r"#(?P<tag_name>[\S]*)"
        content = re.sub(re_pattern, replace, content)
        object.__setattr__(self, "content", content)


@dataclass(frozen=True, order=True)
class ShortPost(FullPost):
    """ Short post data class (the content field is limited to 50 characters) """
    def __post_init__(self):

        content = self.content
        if len(content) > 50:
            r_slice = content.rfind(" ", 0, 50)
            if r_slice == -1:
                r_slice = 50
            content = content[:r_slice] + " ..."

            object.__setattr__(self, "content", content)

        super(ShortPost, self).__post_init__()


class PostHandler(DAO, metaclass=Singleton):
    """ Post handler singleton class (handle database operations) """

    # TODO: Add query caching
    # TODO: If file is not changed and hash of dataclass is exist, return hashed dataclass

    def __init__(self, data_class):
        folder = current_app.config.get("APP_DATA_FOLDER")
        filename = current_app.config.get("APP_DATA_POSTS")
        self._filename = os.path.join(folder, filename)
        self.DataClass = data_class

    def load(self, depth: int = 0) -> list[dataclass]:
        """ Load records from database

        :param depth: How many records you need to upload. If depth <= 0, upload all records. (default=0)
        :return: List of dataclasses
        """
        data = super(PostHandler, self).load(self._filename, depth)
        data = [self.DataClass(**record) for record in data]
        return data

    def save(self, data: list[dataclass]) -> None:
        """ Save records to database

        :param data: List of dataclasses
        :return: None
        """
        data = [asdict(record) for record in data]
        super(PostHandler, self).save(self._filename, data)

    def select_all(self, depth: int = 0):
        """ Select all query

        :param depth: How many records you need to select. If depth <= 0, select all records. (default=0)
        :return: List of dataclasses
        """
        return self.load(depth)

    def select_one_by_pk(self, pk: int) -> dataclass or None:
        """ Select one dataclass by primary key

        :param pk: The primary key
        :return: dataclass or None
        """
        data = super(PostHandler, self).load(self._filename)
        record = super(PostHandler, self).select_one_by_field(data, "pk", pk)
        if record is None:
            return None
        return self.DataClass(**record)

    def select_by_substring(self, substring: str, depth=0) -> list[dataclass]:
        """ Select all dataclasses who contain substring in content

        :param substring: Substring to search
        :param depth: How many records you need to search. If depth <= 0, search in all records. (default=0)
        :return:
        """
        def is_substring(source: str, desc: str) -> bool:
            """ Is substring helper function

            :param source: Source string
            :param desc: Substring
            :return: True or False
            """
            return desc.strip().lower() in source.lower()
        data = super(PostHandler, self).load(self._filename)
        data = super(PostHandler, self).select_all_by_field(data,
                                                            "content", substring,
                                                            is_substring, depth)
        data = [self.DataClass(**record) for record in data]
        return data

    def select_by_username(self, username: str) -> list[dataclass]:
        """ Select all dataclasses who poster_name is equal to username

        :param username: The username
        :return: List of dataclasses
        """

        def is_str_equal(source: str, dest: str) -> bool:
            """ Is source equal to dest

            :param source: The source
            :param dest: The desc
            :return: True or False
            """
            return source.strip().lower() == dest.strip().lower()

        data = super(PostHandler, self).load(self._filename)
        data = super(PostHandler, self).select_all_by_field(data, "poster_name", username, is_str_equal)
        data = [self.DataClass(**record) for record in data]
        return data

    def increment_views_count_by_pk(self, pk: int) -> None:
        """ Increment views count

        :param pk: Primary key
        :return: None
        """

        data = super(PostHandler, self).load(self._filename)
        self.update_field_by_field(data, "pk", pk, "views_count", lambda value: value + 1)
        super(PostHandler, self).save(self._filename, data)

    def increment_likes_count_by_pk(self, pk: int) -> None:
        """ Increment likes count

        :param pk: Primary key
        :return: None
        """

        data = super(PostHandler, self).load(self._filename)
        self.update_field_by_field(data, "pk", pk, "likes_count", lambda value: value + 1)
        super(PostHandler, self).save(self._filename, data)

    def get_posts_count(self) -> int:
        """ Get post count

        :return: Number of posts
        """

        data = super(PostHandler, self).load(self._filename)
        return len(data)

    def get_posts_count_by_substring(self, substring: str) -> int:
        """ Get the number of messages that a substring is part of

        :param substring: The substring
        :return: Number of posts
        """

        def is_substring(source: str, desc: str):
            return desc.strip().lower() in source.lower()
        data = super(PostHandler, self).load(self._filename)
        data = super(PostHandler, self).select_all_by_field(data, "content", substring, is_substring)
        return len(data)

