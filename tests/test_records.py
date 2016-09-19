import pytest
import types

from k9data.common.global_vars import *
from k9data.read_data import *
from k9data.results import *


class TestReadDataFile:
    def test_read_nonexistent_file(self):
        fname = offa_save_path + "/TEST/records-test00.csv"
        with pytest.raises(ValueError):
            read_datafile(fname)

    def test_read_empty_file(self):
        fname = offa_save_path + "/TEST/integrity-test00.csv"
        assert len(read_datafile(fname)) == 0
