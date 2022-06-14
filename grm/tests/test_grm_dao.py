"""
    GRM package
    Tests for grm.dao
"""

# global imports
import os.path
import pytest

# local imports
from grm.dao import DAO


@pytest.fixture
def test_dao_data():
    """ test dao data fixture """
    return [
        {
            "int_field": 1,
            "str_field": "test1",
        },
        {
            "int_field": 2,
            "str_field": "test2",
        },
        {
            "int_field": 3,
            "str_field": "test3",
        }
    ]


class TestDAO(DAO):
    """ Test DAO class """

    def init(self, test_app: object):
        """ Init function """
        filename = "test.json"
        path = test_app.config.get("APP_DATA_FOLDER")
        self.filename = os.path.join(path, filename)

    def save(self):
        """ Save overridden method """
        pass

    def load(self):
        """ Load overridden method """
        pass

    def test_save(self, test_app: object, test_dao_data: dict):
        """ Test DAO save """

        self.init(test_app)

        try:
            super(TestDAO, self).save(self.filename, test_dao_data)

        except Exception as e:
            assert False, f"There should be no exceptions. ({type(e)}: {e})"

    def test_load(self, test_app: object, test_dao_data: dict):
        """ Test DAO load """

        self.init(test_app)

        try:
            data = super(TestDAO, self).load(self.filename)

        except Exception as e:
            assert False, f"There should be no exceptions. ({type(e)}: {e})"

        assert len(data) == len(test_dao_data), "Wrong loaded test dao data"
        assert set([field for record in data for field in record.keys()]) == \
               set([field for record in test_dao_data for field in record.keys()]), \
               "Wrong fields loaded from test dao data"
        assert tuple([(key, value) for record in data for key, value in record.items()]) == \
               tuple([(key, value) for record in test_dao_data for key, value in record.items()]), \
               "Wrong fields: values loaded from test dao data"

    def test_load_deep(self, test_app: object):
        """ Test DAO load with defined depth """

        self.init(test_app)

        try:
            data = super(TestDAO, self).load(self.filename, 2)

        except Exception as e:
            assert False, f"There should be no exceptions. ({type(e)}: {e})"

        assert len(data) == 2, "Must be loaded only 2 records"

    def test_select_all_by_field(self, test_dao_data: dict):
        """ Test DAO select all by field method """

        def is_substring(source, desc):
            return desc in source

        try:

            data_1 = self.select_all_by_field(test_dao_data, "int_field", 1)
            data_2 = self.select_all_by_field(test_dao_data, "str_field", "test", is_substring)

        except Exception as e:
            assert False, f"There should be no exceptions. ({type(e)}: {e})"

        assert len(data_1) == 1, "Wrong selected data"
        assert len(data_2) == 3, "Wrong selected data"

    def test_select_all_by_field_wrong_params(self, test_dao_data: dict):
        """ Test DAO select all by field method with wrong parameters """
        with pytest.raises((KeyError, TypeError)):
            data = self.select_all_by_field(test_dao_data, "expected_field", None)
            data = self.select_all_by_field("test_dao_data", "int_field", 1)
            data = self.select_all_by_field(test_dao_data, "int_field", 1, "one")

        data = self.select_all_by_field(test_dao_data, "int_field", -1)

        assert type(data) is list, "Must be list"
        assert len(data) == 0, "Must be empty"

    def test_select_one_by_field(self, test_dao_data: dict):
        """ Test DAO select one by field method """

        def is_substring(source, desc):
            return desc in source

        try:
            record_1 = self.select_one_by_field(test_dao_data, "int_field", 1)
            record_2 = self.select_one_by_field(test_dao_data, "str_field", "test", is_substring)
            record_3 = self.select_one_by_field(test_dao_data, "str_field", "non-exists")

        except Exception as e:
            assert False, f"There should be no exceptions. ({type(e)}: {e})"

        assert type(record_1) is dict, "Must be a dict"
        assert record_1["int_field"] == 1, "Must be 1"
        assert type(record_2) is dict, "Must be a dict"
        assert record_1["str_field"] == "test1", "Must be 'test1'"
        assert record_3 is None, "Must be a None"

    def test_select_one_by_field_wrong_params(self, test_dao_data: dict):
        """ Test DAO select one by field method with wrong parameters """

        with pytest.raises((KeyError, TypeError)):
            data = self.select_one_by_field(test_dao_data, "expected_field", None)
            data = self.select_one_by_field("test_dao_data", "int_field", 1)
            data = self.select_one_by_field(test_dao_data, "int_field", 1, "one")

        data = self.select_one_by_field(test_dao_data, "int_field", -1)

        assert data is None, "Must be None"

    def test_update_field_by_field(self, test_dao_data: dict):
        """ Test DAO update field by field method """

        try:
            self.update_field_by_field(test_dao_data, "int_field", 1, "str_field", "new_test1")
            self.update_field_by_field(test_dao_data, "int_field", 2, "int_field", lambda i: i + 1)

        except Exception as e:
            assert False, f"There should be no exceptions. ({type(e)}: {e})"

        assert test_dao_data[0]["str_field"] == "new_test1", "Must be 'new_test1'"
        assert test_dao_data[1]["int_field"] == 3, "Must be 3"

    def test_update_field_by_field_wrong_params(self, test_dao_data: dict):
        """ Test DAO update field by field method with wrong parameters """

        with pytest.raises((KeyError, TypeError)):
            self.update_field_by_field(test_dao_data, "expected_field", None, "int_field", 1)
            self.update_field_by_field("test_dao_data", "int_field", 1, "int_field", 2)
            self.update_field_by_field(test_dao_data, "int_field", 1, "expected_field", 2)
