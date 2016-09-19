import pandas as pd

from common.global_vars import breeds
from read_data import *


def list_corrupt(records):
    broken = records.loc[~records["Sex"].isin(["M", "F"])]
    count_broken = len(broken)
    if count_broken:
        print >>sys.stderr, "Corrupt records: " + str(count_broken)
        print >>sys.stderr, broken
    else:
        print >>sys.stderr, "Looking good"
    return count_broken


def main():
    breed_id = os.environ["k9data_breed"] if "k9data_breed" in os.environ else False
    if breed_id:
        records = read_breed(breed_id)
    else:
        for breed_id in breeds:
            breed_records = [read_breed(breed_id) for breed_id in breeds]
        records = pd.concat(breed_records)

    print len(records)
    list_corrupt(records)
    return


if __name__ == "__main__":
    main()
