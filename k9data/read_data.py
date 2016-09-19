import os
import sys
import pandas as pd

from common.global_vars import *
from results import *


def read_datafile(fname):
    if not os.path.exists(fname) or not os.path.isfile(fname):
        raise ValueError("File not found: " + fname)
    try:
        records = pd.read_csv(fname, header=None, names=offa_field_names)
    except:
        raise
    return records


def read_breed(breed_id):
    global offa_save_path

    print >>sys.stderr, "Collecting data for breed", breed_id, ":",

    fdir = offa_save_path + "/" + breed_id
    if not os.path.exists(fdir) or not os.path.isdir(fdir):
        print >>sys.stderr, "wrong location \"" + fdir + "\""
        return

    flist = [d for d in os.listdir(fdir)
             if len(d) > 4 and (d[-4:] == ".csv" or d[-4:] == ".txt")]

    records_list = [read_datafile(fdir + "/" + f) for f in flist]
    records = pd.concat(records_list)
    print >>sys.stderr, "Done."
    return records
