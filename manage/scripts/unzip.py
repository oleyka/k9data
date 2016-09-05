#!/usr/bin/env python

import os
import sys
import urllib2
import zipfile
import types

from global_vars import breeds, offa_save_path


def list_zips(breed_id):
    global breeds
    global offa_save_path

    fdir = offa_save_path + "/" + breed_id
    if not os.path.exists(fdir) or not os.path.isdir(fdir):
        return

    return [d for d in os.listdir(fdir) if (len(d) > 4 and d[-4:] == ".zip")]


def unzip_list(breed_id, flist):
    if flist is None:
        return
    for f in flist:
        logstr("Unpack " + f + " into " + offa_save_path + "/" + breed_id + ": ")
        fpath = offa_save_path + "/" + breed_id + "/" + f
        zip_ref = zipfile.ZipFile(fpath, 'r')
        zip_ref.extractall(offa_save_path + "/" + breed_id)
        zip_ref.close()
        print >>sys.stderr, logstr + "OK"


def main():
    global breeds, offa_save_path

    for breed_id in breeds:
        unzip_list(breed_id, list_zips(breed_id))


if __name__ == "__main__":
    main()
