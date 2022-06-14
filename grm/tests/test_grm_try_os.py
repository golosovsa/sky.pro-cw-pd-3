"""
    GRM package
    Tests for grm.patterns
"""

# global imports
import os
import pytest
from werkzeug.exceptions import HTTPException, InternalServerError

# local imports
from ..try_os import try_os_io


def test_grm_try_os_not_exists(test_app):
    """ Test try os decorator if file not exists """

    @try_os_io
    def test_try_os_io(filename):
        with open(filename, "rt", encoding="utf-8"):
            pass

    with pytest.raises(HTTPException):
        test_try_os_io("not-exists.txt")


def test_grm_try_os_busy(test_app):
    """ Test try os decorator if file is busy """

    @try_os_io
    def test_try_os_io(filename):
        fin = open(filename, "wt", encoding="utf-8")
        data = fin.read()
        fin.close()

    fou = open("tests/test_file.txt", "wt", encoding="utf-8")

    with pytest.raises(HTTPException):
        test_try_os_io("tests/test_file.txt")

    fou.close()
