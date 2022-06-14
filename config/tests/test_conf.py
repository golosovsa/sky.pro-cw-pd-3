"""
    Coursework №3
    Golosov_SA aka grm
    link: https://skyengpublic.notion.site/3-d2893a166cf0479a8c8bb3bfb13d478e#70281dd53e6e4930843e2501562a72f2

   Test config file
"""

# global imports
import pytest

# local imports
from ..base import BaseConfig
from ..development import DevelopmentConfig
from ..testing import TestingConfig


class TestConfig:
    """ Test config class """

    @pytest.mark.parametrize(
        "attr, value",
        [
            ("APP_DATA_FOLDER", ""),
            ("APP_DATA_POSTS", "posts.json"),
            ("APP_DATA_COMMENTS", "comments.json"),
            ("APP_DATA_BOOKMARKS", "bookmarks.json"),
            ("IO_ATTEMPTS", 10),
            ("IO_SLEEP_FOR", 0.2),
            ("SEARCH_DEPTH", 10),
            ("JSON_AS_ASCII", False),
            ("APP_LOG_DIR", "logs/"),
            ("APP_LOG_EXCEPTION_ERRORS_FILE", "errors.log"),
            ("APP_LOG_API_USAGE_FILE", "api.log"),
            ("APP_LOG_USER_ACTIVITY_FILE", "user.log"),
        ]
    )
    def test_base_config_has_attr(self, attr, value):
        """ Test base config has attr """

        base_config = BaseConfig()

        assert hasattr(base_config, attr), "Attr missing"
        attr_value = getattr(base_config, attr)
        assert type(attr_value) == type(value), "Types must be equal"
        assert attr_value == value, "Must be equal"

    def test_base_config_wrong_attr(self):
        """ Test base config has no attr """
        base_config = BaseConfig()

        assert not hasattr(base_config, "TESTING"), "Wrong attr"

    @pytest.mark.parametrize(
        "attr, value",
        [
            ("APP_DATA_FOLDER", "./data"),
            ("APP_DATA_POSTS", "posts.json"),
            ("APP_DATA_COMMENTS", "comments.json"),
            ("APP_DATA_BOOKMARKS", "bookmarks.json"),
            ("IO_ATTEMPTS", 10),
            ("IO_SLEEP_FOR", 0.2),
            ("SEARCH_DEPTH", 10),
            ("JSON_AS_ASCII", False),
            ("APP_LOG_DIR", "logs/"),
            ("APP_LOG_EXCEPTION_ERRORS_FILE", "errors.log"),
            ("APP_LOG_API_USAGE_FILE", "api.log"),
            ("APP_LOG_USER_ACTIVITY_FILE", "user.log"),
        ]
    )
    def test_development_config_has_attr(self, attr, value):
        """ Test developing config has attr """
        development_config = DevelopmentConfig()

        assert hasattr(development_config, attr), "Attr missing"
        attr_value = getattr(development_config, attr)
        assert type(attr_value) == type(value), "Types must be equal"
        assert attr_value == value, "Must be equal"

    def test_development_config_wrong_attr(self):
        """ Test developing config has no attr """

        development_config = DevelopmentConfig()

        assert not hasattr(development_config, "TESTING"), "Wrong attr"

    @pytest.mark.parametrize(
        "attr, value",
        [
            ("APP_DATA_FOLDER", "./tests/data"),
            ("APP_DATA_POSTS", "posts.json"),
            ("APP_DATA_COMMENTS", "comments.json"),
            ("APP_DATA_BOOKMARKS", "bookmarks.json"),
            ("IO_ATTEMPTS", 10),
            ("IO_SLEEP_FOR", 0.2),
            ("SEARCH_DEPTH", 10),
            ("JSON_AS_ASCII", False),
            ("APP_LOG_DIR", "logs/"),
            ("APP_LOG_EXCEPTION_ERRORS_FILE", "errors.log"),
            ("APP_LOG_API_USAGE_FILE", "api.log"),
            ("APP_LOG_USER_ACTIVITY_FILE", "user.log"),
            ("TESTING", True),
        ]
    )
    def test_testing_config_has_attr(self, attr, value):
        """ Test testing config has attr """

        testing_config = TestingConfig()

        assert hasattr(testing_config, attr), "Attr missing"
        attr_value = getattr(testing_config, attr)
        assert type(attr_value) == type(value), "Types must be equal"
        assert attr_value == value, "Must be equal"
