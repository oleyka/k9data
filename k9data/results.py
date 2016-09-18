import pandas as pd


def count_hd_by_result(records):
    res_str = ""

    res_str += "HD records stats:\n"
    hd_results = records.loc[lambda df: df["Registry Code"] == "HD", :]
    ghd_results = records.loc[lambda df: df["Registry Code"] == "GHD", :]
    ohd_results = records.loc[lambda df: df["Registry Code"] == "OHD", :]
    phd_results = records.loc[lambda df: df["Registry Code"] == "PHD", :]
    hd_all_results = pd.concat([hd_results, ghd_results, ohd_results, phd_results])
    res_str += str(hd_all_results.groupby("Results")["Results"].count().sort_values())
    res_str += "Total HD records:"
    res_str += str(hd_all_results["Results"].count())
    return res_str

    '''  NOTE looking up broken records
    hd_results = records.loc[lambda df: df["Registry Code"] == "HD", :].groupby(["Results"])["Results"]
    print hd_results.loc[lambda df: df["Results"] == "12/11/2001", :] #.count()
    '''
