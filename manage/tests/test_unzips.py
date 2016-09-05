#!/usr/bin/env python

import pytest
import types

from scripts.unzip import *


class TestUnzip:
    def test_list_nonexistent_dir(self):
        assert list_zips('XO') is None

    def test_list_no_zips(self):
        nzlist = list_zips('ALH')
        assert isinstance(nzlist, types.ListType)
        assert len(nzlist) == 0

    def test_list_three_zips(self):
        thlist = list_zips('BEC')
        assert isinstance(thlist, types.ListType)
        assert len(thlist) == 3
        assert 'BEC30-Sep-04.zip' in thlist
