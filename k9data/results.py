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


def count_tests(records):
    print "Test counts:"
    print records.groupby(["Registry Code"])["Registry Code"].count().sort_values()


def main():
    breed_id = os.environ["k9data_breed"] if "k9data_breed" in os.environ else False
    if breed_id:
        records = read_breed(breed_id)
    else:
        for breed_id in breeds:
            breed_records = [read_breed(breed_id) for breed_id in breeds]
        records = pd.concat(breed_records)

    print len(records)
    print count_hd_by_result(records)
    return


if __name__ == "__main__":
    main()
