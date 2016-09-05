#!/usr/bin/env python

import pytest
from scripts.download import *
from scripts.global_vars import *


def test_fileinfo_missing():
    assert get_filename(None) is None


def test_fileinfo_malformed():
    assert get_filename('attachment; ;; filename=///PO30///$ -jun-16.csv') is None


def test_fileinfo_sanitize():
    assert get_filename('attachment; filename=///PO30///$ -jun-16.csv')  == save_path + 'PO30-jun-16.csv'


def test_report_missing():
    assert get_offa_data("web31-Mar-96up.zip", "WO") is None


def test_report_repeat_download():
    get_offa_data("web31-Mar-96up.zip", "PO")
    assert get_offa_data("web31-Mar-96up.zip", "PO") is None
