#!/usr/bin/env python

import os
import sys
import pandas as pd

from common.global_vars import *


def read_all(breed_id):
    global offa_save_path

    print >>sys.stderr, "Collecting data for breed", breed_id, ":",

    fdir = offa_save_path + "/" + breed_id
    if not os.path.exists(fdir) or not os.path.isdir(fdir):
        print >>sys.stderr, "wrong location \"" + fdir + "\""
        return

    flist = [d for d in os.listdir(fdir)
             if len(d) > 4 and (d[-4:] == ".csv" or d[-4:] == ".txt")]

    records_list = [pd.read_csv(fdir + "/" + f,
                                header=None,
                                skip_blank_lines=True,
                                names=[
                                    "OFA Number",
                                    "Registration Number",
                                    "Registry Code",
                                    "Closed/Open",
                                    "Breed Code",
                                    "Registered Name",
                                    "Sex",
                                    "Color",
                                    "Birthdate",
                                    "Age at Test (Months)",
                                    "Test Date",
                                    "Results",
                                    "Sire Registration",
                                    "Dam Registration",
                                    "CHIC Number"
                                ]) for f in flist]

    records = pd.concat(records_list)
    print >>sys.stderr, "Done."
    return records


def count_tests(records):
    print "Test counts:"
    print records.groupby(["Registry Code"])["Registry Code"].count().sort_values()


def count_hd_results(records):
    print "HD records stats:"
    hd_results = records.loc[lambda df: df["Registry Code"] == "HD", :]
    ghd_results = records.loc[lambda df: df["Registry Code"] == "GHD", :]
    ohd_results = records.loc[lambda df: df["Registry Code"] == "OHD", :]
    phd_results = records.loc[lambda df: df["Registry Code"] == "PHD", :]
    hd_all_results = pd.concat([hd_results, ghd_results, ohd_results, phd_results])
    print hd_all_results.groupby("Results")["Results"].count().sort_values()
    print "Total HD records:", hd_all_results["Results"].count()

    '''  NOTE looking up broken records
    hd_results = records.loc[lambda df: df["Registry Code"] == "HD", :].groupby(["Results"])["Results"]
    print hd_results.loc[lambda df: df["Results"] == "12/11/2001", :] #.count()
    '''


def main():
    breed_id = os.environ["k9data_breed"] if "k9data_breed" in os.environ else "WO"
    records = read_all(breed_id)
    count_hd_results(records)

    '''  NOTE read them all
    codes = set()
    for breed_id in breeds:
        records = read_all(breed_id)
        if records is not None:
            print records["Registry Code"].unique()
            codes.update(records["Registry Code"].unique().tolist())
    print "Collected codes", sorted(codes)
    '''
    return

if __name__ == "__main__":
    main()
