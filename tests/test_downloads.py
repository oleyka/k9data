#!/usr/bin/env python

import pytest
from k9data.download import *
from k9data.common.global_vars import offa_save_path


class TestDownloads:
    def test_fileinfo_missing(self):
        assert get_filename(None, "PO") is None

    def test_fileinfo_malformed(self):
        assert get_filename("attachment; ;; filename=///PO30///$ -jun-16.csv", "PO") is None

    def test_breedinfo_missing(self):
        global offa_save_path
        assert get_filename("attachment; filename=PO30-jun-16.csv", None) == offa_save_path + "/PO30-jun-16.csv"

    def test_fileinfo_sanitize(self):
        global offa_save_path
        assert get_filename("attachment; filename=///PO30///$ -jun-16.csv", "PO")  == offa_save_path + "/PO/PO30-jun-16.csv"

    def test_report_missing(self):
        assert get_offa_data("web31-Mar-96up.zip", "WO") is None

    def test_report_repeat_download(self):
        get_offa_data("web31-Mar-96up.zip", "PO")
        assert get_offa_data("web31-Mar-96up.zip", "PO") is None
