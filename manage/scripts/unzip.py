#!/usr/bin/env python

import os
import sys
import urllib2
import zipfile

from global_vars import breeds, save_path


def list_zips(breed_id):
    global breeds
    global save_path

    fdir = save_path + "/" + breed_id

    if not os.path.exists(fdir) or not os.path.isdir(fdir):
        return

    ziplist = [d for d in os.listdir(fdir) if (len(d) > 4 and d[-4:] == ".zip")]

    return ziplist


def unzip_list(breed_id, flist):
    if flist is None:
        return
    for f in flist:
        fpath = save_path + "/" + breed_id + "/" + f
        zip_ref = zipfile.ZipFile(fpath, 'r')
        zip_ref.extractall(save_path + "/" + breed_id)
        zip_ref.close()


def main():
    global breeds

    for breed_id in breeds:
        unzip_list(breed_id, list_zips(breed_id))


if __name__ == "__main__":
    main()
